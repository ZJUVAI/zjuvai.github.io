#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版论文信息爬虫
只使用Python标准库，无需额外依赖

Usage:
    python simple_paper_crawler.py "论文标题"
"""

import os
import re
import sys
import json
import time
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from typing import Dict, List, Optional


class SimplePaperCrawler:
    """简化版论文信息爬虫类（仅使用标准库）"""
    
    def __init__(self, output_dir: str = None):
        self.output_dir = output_dir or "content/publications"
        
    def search_semantic_scholar(self, title: str) -> Optional[Dict]:
        """从Semantic Scholar搜索论文信息"""
        try:
            # 构建查询URL
            base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
            params = {
                'query': title,
                'limit': '1',
                'fields': 'title,authors,abstract,year,venue,url,citationCount,fieldsOfStudy,publicationDate,journal,doi'
            }
            
            query_string = urllib.parse.urlencode(params)
            url = f"{base_url}?{query_string}"
            
            # 发送请求
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            req = urllib.request.Request(url, headers=headers)
            
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.getcode() != 200:
                    return None
                
                data = json.loads(response.read().decode('utf-8'))
                
            if not data.get('data'):
                return None
                
            paper = data['data'][0]
            paper_info = {}
            
            # 基本信息
            paper_info['title'] = paper.get('title', '')
            paper_info['abstract'] = paper.get('abstract', '')
            paper_info['year'] = paper.get('year', '')
            paper_info['venue'] = paper.get('venue', '')
            paper_info['doi'] = paper.get('doi', '')
            paper_info['url'] = paper.get('url', '')
            paper_info['citation_count'] = paper.get('citationCount', 0)
            
            # 作者信息
            authors = []
            if paper.get('authors'):
                for author in paper['authors']:
                    authors.append(author.get('name', ''))
            paper_info['authors'] = authors
            
            # 发布日期
            if paper.get('publicationDate'):
                paper_info['date'] = paper['publicationDate']
            elif paper.get('year'):
                paper_info['date'] = f"{paper['year']}-01-01"
            
            # 期刊信息
            if paper.get('journal'):
                paper_info['journal'] = paper['journal'].get('name', '')
            
            # 研究领域
            if paper.get('fieldsOfStudy'):
                paper_info['fields'] = paper['fieldsOfStudy']
            
            paper_info['source'] = 'semantic_scholar'
            return paper_info
            
        except Exception as e:
            print(f"Semantic Scholar搜索失败: {e}")
            return None
    
    def search_paper(self, title: str) -> Optional[Dict]:
        """搜索论文信息"""
        print(f"正在搜索论文: {title}")
        print("  - 搜索 Semantic Scholar...")
        
        paper_info = self.search_semantic_scholar(title)
        if paper_info:
            print("    ✓ 找到结果")
            return paper_info
        else:
            print("    ✗ 未找到结果")
            return None
    
    def clean_filename(self, name: str) -> str:
        """清理文件名，移除非法字符"""
        # 移除或替换非法字符
        cleaned = re.sub(r'[<>:"/\\|?*]', '', name)
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        # 限制长度
        if len(cleaned) > 100:
            cleaned = cleaned[:100].rsplit(' ', 1)[0]
        return cleaned
    
    def generate_folder_name(self, paper_info: Dict) -> str:
        """生成文件夹名称"""
        title = paper_info.get('title', '').strip()
        if not title:
            return "untitled_paper"
        
        # 清理标题作为文件夹名
        folder_name = self.clean_filename(title)
        
        # 如果标题太长，尝试使用更短的版本
        if len(folder_name) > 80:
            # 尝试只使用前几个单词
            words = folder_name.split()[:8]
            folder_name = ' '.join(words)
        
        return folder_name
    
    def create_simple_bibtex(self, paper_info: Dict) -> str:
        """生成简单的BibTeX引用"""
        # 生成引用key
        first_author = ""
        if paper_info.get('authors'):
            first_author = paper_info['authors'][0].split()[-1].lower()  # 姓氏
        year = ""
        if paper_info.get('date'):
            year = paper_info['date'][:4]
        elif paper_info.get('year'):
            year = str(paper_info['year'])
        
        title_words = paper_info.get('title', '').lower().split()[:2]
        title_part = ''.join(word for word in title_words if word.isalnum())
        
        entry_id = f"{first_author}{year}{title_part}"
        
        # 构建BibTeX
        bibtex = f"@article{{{entry_id},\n"
        
        if paper_info.get('title'):
            bibtex += f"  title = {{{paper_info['title']}}},\n"
        
        if paper_info.get('authors'):
            author_str = ' and '.join(paper_info['authors'])
            bibtex += f"  author = {{{author_str}}},\n"
        
        if year:
            bibtex += f"  year = {{{year}}},\n"
        
        if paper_info.get('journal'):
            bibtex += f"  journal = {{{paper_info['journal']}}},\n"
        elif paper_info.get('venue'):
            bibtex += f"  journal = {{{paper_info['venue']}}},\n"
        
        if paper_info.get('doi'):
            bibtex += f"  doi = {{{paper_info['doi']}}},\n"
        
        if paper_info.get('url'):
            bibtex += f"  url = {{{paper_info['url']}}},\n"
        
        bibtex += "}\n"
        return bibtex
    
    def create_hugo_content(self, paper_info: Dict) -> str:
        """生成Hugo前言内容"""
        content = "---\n"
        content += "# Documentation: https://sourcethemes.com/academic/docs/managing-content/\n\n"
        
        # 标题
        title = paper_info.get('title', 'Untitled Paper')
        content += f'title: "{title}"\n'
        
        # 作者
        if paper_info.get('authors'):
            content += "authors:\n"
            content += "  [\n"
            for author in paper_info['authors']:
                content += f"    {author},\n"
            content += "  ]\n"
        
        # 日期
        date = paper_info.get('date', '2024-01-01')
        # 确保日期格式正确
        if len(date) == 10:  # YYYY-MM-DD
            content += f'date: {date}T08:00:00+08:00\n'
        else:
            content += f'date: 2024-01-01T08:00:00+08:00\n'
        
        # DOI
        doi = paper_info.get('doi', '')
        content += f'doi: "{doi}"\n\n'
        
        # 发表类型
        content += "# Publication type.\n"
        content += "# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;\n"
        content += "# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;\n"
        content += "# 7 = Thesis; 8 = Patent\n"
        content += 'publication_types: ["2"]\n\n'  # 默认期刊文章
        
        # 发表信息
        publication = paper_info.get('journal') or paper_info.get('venue', '')
        content += f'publication: "{publication}"\n'
        content += f'publication_short: "{publication}"\n\n'
        
        # 摘要
        abstract = paper_info.get('abstract', '')
        # 转义引号并限制长度
        abstract = abstract.replace('"', '\\"').replace('\n', ' ').strip()
        if len(abstract) > 1000:
            abstract = abstract[:1000] + "..."
        content += f'abstract: "{abstract}"\n\n'
        
        # 总结（可选）
        content += 'summary: ""\n\n'
        
        # 标签
        content += "tags:\n"
        if paper_info.get('fields'):
            content += "  [\n"
            for field in paper_info['fields'][:5]:  # 最多5个标签
                content += f'    "{field}",\n'
            content += "  ]\n"
        else:
            content += '  ["Research"]\n'
        
        content += "categories: []\n"
        content += "featured: false\n\n"
        
        # URL链接
        url = paper_info.get('url', '')
        content += f"url_pdf: \"{url}\"\n"
        content += "url_code:\n"
        content += "url_dataset:\n"
        content += "url_poster:\n"
        content += "url_project:\n"
        content += "url_slides:\n"
        content += "url_source:\n"
        content += "url_video:\n\n"
        
        # 特色图片
        content += "# Featured image\n"
        content += "image:\n"
        content += '  caption: ""\n'
        content += '  focal_point: ""\n'
        content += "  preview_only: false\n\n"
        
        # 关联项目和幻灯片
        content += "projects: []\n"
        content += 'slides: ""\n'
        content += "---\n\n"
        
        return content
    
    def create_paper_folder(self, paper_info: Dict) -> bool:
        """为论文创建完整的文件夹结构"""
        try:
            # 生成文件夹名
            folder_name = self.generate_folder_name(paper_info)
            output_folder = Path(self.output_dir) / folder_name
            
            # 检查文件夹是否已存在
            if output_folder.exists():
                print(f"警告: 文件夹 '{folder_name}' 已存在")
                response = input("是否覆盖? (y/N): ").strip().lower()
                if response != 'y':
                    print("取消操作")
                    return False
            
            # 创建文件夹
            output_folder.mkdir(parents=True, exist_ok=True)
            
            # 创建index.md
            hugo_content = self.create_hugo_content(paper_info)
            index_file = output_folder / "index.md"
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(hugo_content)
            
            # 创建featured.bib
            bibtex_content = self.create_simple_bibtex(paper_info)
            bib_file = output_folder / "featured.bib"
            with open(bib_file, 'w', encoding='utf-8') as f:
                f.write(bibtex_content)
            
            print(f"✓ 成功创建论文文件夹: {output_folder}")
            print(f"  - index.md: Hugo内容文件")
            print(f"  - featured.bib: BibTeX引用文件")
            
            # 显示论文信息摘要
            print(f"\n论文信息摘要:")
            print(f"  标题: {paper_info.get('title', 'N/A')}")
            print(f"  作者: {', '.join(paper_info.get('authors', []))}")
            print(f"  发表: {paper_info.get('journal') or paper_info.get('venue', 'N/A')}")
            print(f"  年份: {paper_info.get('date', paper_info.get('year', 'N/A'))}")
            
            return True
            
        except Exception as e:
            print(f"创建文件夹失败: {e}")
            return False


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python simple_paper_crawler.py \"论文标题\"")
        sys.exit(1)
    
    title = sys.argv[1]
    crawler = SimplePaperCrawler()
    
    paper_info = crawler.search_paper(title)
    
    if paper_info:
        success = crawler.create_paper_folder(paper_info)
        if success:
            print("✓ 操作完成!")
            sys.exit(0)
        else:
            print("✗ 操作失败!")
            sys.exit(1)
    else:
        print("✗ 未找到论文信息")
        print("提示: 尝试使用完整的英文标题")
        sys.exit(1)


if __name__ == "__main__":
    main()
