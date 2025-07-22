#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper Information Crawler and Hugo Content Generator
自动爬取论文信息并为Hugo网站生成相应的content结构

Usage:
    python paper_crawler.py "论文标题"
    python paper_crawler.py --interactive
"""

import os
import re
import sys
import json
import time
import argparse
import requests
import urllib.parse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase


class PaperCrawler:
    """论文信息爬虫类"""
    
    def __init__(self, output_dir: str = None):
        self.output_dir = output_dir or "content/publications"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def search_arxiv(self, title: str) -> Optional[Dict]:
        """从arXiv搜索论文信息"""
        try:
            # arXiv API查询
            base_url = "http://export.arxiv.org/api/query"
            query = f'ti:"{title}"'
            params = {
                'search_query': query,
                'start': 0,
                'max_results': 1,
                'sortBy': 'relevance',
                'sortOrder': 'descending'
            }
            
            response = self.session.get(base_url, params=params, timeout=30)
            if response.status_code != 200:
                return None
                
            # 解析XML响应
            import xml.etree.ElementTree as ET
            root = ET.fromstring(response.content)
            
            entries = root.findall('.//{http://www.w3.org/2005/Atom}entry')
            if not entries:
                return None
                
            entry = entries[0]
            
            # 提取信息
            paper_info = {}
            
            # 标题
            title_elem = entry.find('.//{http://www.w3.org/2005/Atom}title')
            paper_info['title'] = title_elem.text.strip() if title_elem is not None else ""
            
            # 作者
            authors = []
            for author in entry.findall('.//{http://www.w3.org/2005/Atom}author'):
                name_elem = author.find('.//{http://www.w3.org/2005/Atom}name')
                if name_elem is not None:
                    authors.append(name_elem.text.strip())
            paper_info['authors'] = authors
            
            # 摘要
            summary_elem = entry.find('.//{http://www.w3.org/2005/Atom}summary')
            paper_info['abstract'] = summary_elem.text.strip() if summary_elem is not None else ""
            
            # 发布日期
            published_elem = entry.find('.//{http://www.w3.org/2005/Atom}published')
            if published_elem is not None:
                paper_info['date'] = published_elem.text[:10]  # YYYY-MM-DD
            
            # PDF链接
            for link in entry.findall('.//{http://www.w3.org/2005/Atom}link'):
                if link.get('type') == 'application/pdf':
                    paper_info['pdf_url'] = link.get('href')
                    break
            
            # arXiv ID
            id_elem = entry.find('.//{http://www.w3.org/2005/Atom}id')
            if id_elem is not None:
                arxiv_id = id_elem.text.split('/')[-1]
                paper_info['arxiv_id'] = arxiv_id
            
            # 分类
            categories = []
            for category in entry.findall('.//{http://arxiv.org/schemas/atom}primary_category'):
                categories.append(category.get('term'))
            for category in entry.findall('.//{http://arxiv.org/schemas/atom}category'):
                cat_term = category.get('term')
                if cat_term not in categories:
                    categories.append(cat_term)
            paper_info['categories'] = categories
            
            paper_info['source'] = 'arxiv'
            return paper_info
            
        except Exception as e:
            print(f"arXiv搜索失败: {e}")
            return None
    
    def search_semantic_scholar(self, title: str) -> Optional[Dict]:
        """从Semantic Scholar搜索论文信息"""
        try:
            base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
            params = {
                'query': title,
                'limit': 1,
                'fields': 'title,authors,abstract,year,venue,url,citationCount,referenceCount,fieldsOfStudy,publicationDate,journal,publicationTypes,doi'
            }
            
            response = self.session.get(base_url, params=params, timeout=30)
            if response.status_code != 200:
                return None
                
            data = response.json()
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
            
            # 发表类型
            if paper.get('publicationTypes'):
                paper_info['publication_types'] = paper['publicationTypes']
            
            paper_info['source'] = 'semantic_scholar'
            return paper_info
            
        except Exception as e:
            print(f"Semantic Scholar搜索失败: {e}")
            return None
    
    def search_crossref(self, title: str) -> Optional[Dict]:
        """从Crossref搜索论文信息"""
        try:
            base_url = "https://api.crossref.org/works"
            params = {
                'query.title': title,
                'rows': 1,
                'select': 'title,author,abstract,published-print,published-online,container-title,DOI,URL,type,subject'
            }
            
            response = self.session.get(base_url, params=params, timeout=30)
            if response.status_code != 200:
                return None
                
            data = response.json()
            if not data.get('message', {}).get('items'):
                return None
                
            paper = data['message']['items'][0]
            paper_info = {}
            
            # 标题
            if paper.get('title'):
                paper_info['title'] = paper['title'][0]
            
            # 作者
            authors = []
            if paper.get('author'):
                for author in paper['author']:
                    given = author.get('given', '')
                    family = author.get('family', '')
                    if given and family:
                        authors.append(f"{given} {family}")
                    elif family:
                        authors.append(family)
            paper_info['authors'] = authors
            
            # 摘要
            if paper.get('abstract'):
                paper_info['abstract'] = paper['abstract']
            
            # DOI
            if paper.get('DOI'):
                paper_info['doi'] = paper['DOI']
                paper_info['url'] = f"https://doi.org/{paper['DOI']}"
            
            # 期刊/会议
            if paper.get('container-title'):
                paper_info['journal'] = paper['container-title'][0]
            
            # 发布日期
            pub_date = paper.get('published-print') or paper.get('published-online')
            if pub_date and pub_date.get('date-parts'):
                date_parts = pub_date['date-parts'][0]
                if len(date_parts) >= 3:
                    paper_info['date'] = f"{date_parts[0]:04d}-{date_parts[1]:02d}-{date_parts[2]:02d}"
                elif len(date_parts) >= 2:
                    paper_info['date'] = f"{date_parts[0]:04d}-{date_parts[1]:02d}-01"
                elif len(date_parts) >= 1:
                    paper_info['date'] = f"{date_parts[0]:04d}-01-01"
            
            # 发表类型
            if paper.get('type'):
                paper_info['type'] = paper['type']
            
            # 学科分类
            if paper.get('subject'):
                paper_info['subjects'] = paper['subject']
            
            paper_info['source'] = 'crossref'
            return paper_info
            
        except Exception as e:
            print(f"Crossref搜索失败: {e}")
            return None
    
    def search_dblp(self, title: str) -> Optional[Dict]:
        """从DBLP搜索论文信息"""
        try:
            base_url = "https://dblp.org/search/publ/api"
            params = {
                'q': title,
                'format': 'json',
                'h': 1
            }
            
            response = self.session.get(base_url, params=params, timeout=30)
            if response.status_code != 200:
                return None
                
            data = response.json()
            if not data.get('result', {}).get('hits', {}).get('hit'):
                return None
                
            paper = data['result']['hits']['hit'][0]['info']
            paper_info = {}
            
            # 标题
            paper_info['title'] = paper.get('title', '')
            
            # 作者
            authors = []
            if paper.get('authors'):
                author_info = paper['authors']['author']
                if isinstance(author_info, list):
                    for author in author_info:
                        if isinstance(author, dict):
                            authors.append(author.get('text', ''))
                        else:
                            authors.append(str(author))
                else:
                    if isinstance(author_info, dict):
                        authors.append(author_info.get('text', ''))
                    else:
                        authors.append(str(author_info))
            paper_info['authors'] = authors
            
            # 发布年份
            if paper.get('year'):
                paper_info['year'] = paper['year']
                paper_info['date'] = f"{paper['year']}-01-01"
            
            # 期刊/会议
            if paper.get('venue'):
                paper_info['venue'] = paper['venue']
            
            # DOI
            if paper.get('doi'):
                paper_info['doi'] = paper['doi']
                paper_info['url'] = f"https://doi.org/{paper['doi']}"
            
            # DBLP URL
            if paper.get('url'):
                paper_info['dblp_url'] = paper['url']
            
            paper_info['source'] = 'dblp'
            return paper_info
            
        except Exception as e:
            print(f"DBLP搜索失败: {e}")
            return None
    
    def merge_paper_info(self, paper_infos: List[Dict]) -> Dict:
        """合并多个来源的论文信息"""
        merged = {}
        
        # 优先级: Semantic Scholar > Crossref > DBLP > arXiv
        priority_sources = ['semantic_scholar', 'crossref', 'dblp', 'arxiv']
        
        # 按优先级排序
        paper_infos.sort(key=lambda x: priority_sources.index(x.get('source', 'unknown')) 
                        if x.get('source') in priority_sources else len(priority_sources))
        
        for info in paper_infos:
            for key, value in info.items():
                if key == 'source':
                    continue
                if key not in merged or not merged[key]:
                    merged[key] = value
                elif key == 'authors' and isinstance(value, list) and len(value) > len(merged.get(key, [])):
                    merged[key] = value
                elif key == 'abstract' and len(str(value)) > len(str(merged.get(key, ''))):
                    merged[key] = value
        
        # 记录来源
        merged['sources'] = [info.get('source') for info in paper_infos if info.get('source')]
        
        return merged
    
    def search_paper(self, title: str) -> Optional[Dict]:
        """搜索论文信息（多来源）"""
        print(f"正在搜索论文: {title}")
        
        paper_infos = []
        
        # 搜索各个数据源
        print("  - 搜索 Semantic Scholar...")
        ss_info = self.search_semantic_scholar(title)
        if ss_info:
            paper_infos.append(ss_info)
            print("    ✓ 找到结果")
        else:
            print("    ✗ 未找到结果")
        
        time.sleep(1)  # 避免请求过于频繁
        
        print("  - 搜索 arXiv...")
        arxiv_info = self.search_arxiv(title)
        if arxiv_info:
            paper_infos.append(arxiv_info)
            print("    ✓ 找到结果")
        else:
            print("    ✗ 未找到结果")
        
        time.sleep(1)
        
        print("  - 搜索 Crossref...")
        crossref_info = self.search_crossref(title)
        if crossref_info:
            paper_infos.append(crossref_info)
            print("    ✓ 找到结果")
        else:
            print("    ✗ 未找到结果")
        
        time.sleep(1)
        
        print("  - 搜索 DBLP...")
        dblp_info = self.search_dblp(title)
        if dblp_info:
            paper_infos.append(dblp_info)
            print("    ✓ 找到结果")
        else:
            print("    ✗ 未找到结果")
        
        if not paper_infos:
            print("  ✗ 所有数据源都未找到结果")
            return None
        
        # 合并信息
        merged_info = self.merge_paper_info(paper_infos)
        print(f"  ✓ 成功合并来自 {len(paper_infos)} 个数据源的信息")
        
        return merged_info
    
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
    
    def create_bibtex(self, paper_info: Dict) -> str:
        """生成BibTeX引用"""
        # 创建数据库
        db = BibDatabase()
        
        # 确定论文类型
        entry_type = 'article'
        if paper_info.get('type') == 'proceedings-article' or paper_info.get('venue'):
            if any(word in str(paper_info.get('venue', '')).lower() 
                  for word in ['conference', 'proceedings', 'workshop', 'symposium']):
                entry_type = 'inproceedings'
        
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
        
        # 创建条目
        entry = {
            'ENTRYTYPE': entry_type,
            'ID': entry_id,
        }
        
        # 添加字段
        if paper_info.get('title'):
            entry['title'] = paper_info['title']
        
        if paper_info.get('authors'):
            entry['author'] = ' and '.join(paper_info['authors'])
        
        if year:
            entry['year'] = year
        
        if paper_info.get('journal'):
            entry['journal'] = paper_info['journal']
        elif paper_info.get('venue'):
            if entry_type == 'inproceedings':
                entry['booktitle'] = paper_info['venue']
            else:
                entry['journal'] = paper_info['venue']
        
        if paper_info.get('doi'):
            entry['doi'] = paper_info['doi']
        
        if paper_info.get('url'):
            entry['url'] = paper_info['url']
        
        if paper_info.get('abstract'):
            entry['abstract'] = paper_info['abstract']
        
        db.entries = [entry]
        
        # 生成BibTeX字符串
        writer = BibTexWriter()
        writer.indent = '  '
        return writer.write(db)
    
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
        
        # 根据信息推断发表类型
        pub_type = "0"  # 默认未分类
        if paper_info.get('type') == 'proceedings-article' or \
           (paper_info.get('venue') and 
            any(word in str(paper_info.get('venue', '')).lower() 
                for word in ['conference', 'proceedings', 'workshop', 'symposium'])):
            pub_type = "1"  # 会议论文
        elif paper_info.get('journal') or \
             (paper_info.get('venue') and 
              any(word in str(paper_info.get('venue', '')).lower() 
                  for word in ['journal', 'transactions', 'letters'])):
            pub_type = "2"  # 期刊文章
        elif 'arxiv' in paper_info.get('sources', []):
            pub_type = "3"  # 预印本
        
        content += f'publication_types: ["{pub_type}"]\n\n'
        
        # 发表信息
        publication = paper_info.get('journal') or paper_info.get('venue', '')
        content += f'publication: "{publication}"\n'
        content += f'publication_short: "{publication}"\n\n'
        
        # 摘要
        abstract = paper_info.get('abstract', '')
        # 转义引号
        abstract = abstract.replace('"', '\\"').replace('\n', ' ').strip()
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
        elif paper_info.get('subjects'):
            content += "  [\n"
            for subject in paper_info['subjects'][:5]:
                content += f'    "{subject}",\n'
            content += "  ]\n"
        else:
            content += '  ["Research"]\n'
        
        content += "categories: []\n"
        content += "featured: false\n\n"
        
        # 自定义链接
        content += "# Custom links (optional).\n"
        content += "#   Uncomment and edit lines below to show custom links.\n"
        content += "# links:\n"
        content += "# - name: Follow\n"
        content += "#   url: https://twitter.com\n"
        content += "#   icon_pack: fab\n"
        content += "#   icon: twitter\n\n"
        
        # URL链接
        pdf_url = paper_info.get('pdf_url', '')
        if not pdf_url and paper_info.get('url'):
            pdf_url = paper_info['url']
        
        content += f"url_pdf: \"{pdf_url}\"\n"
        content += "url_code:\n"
        content += "url_dataset:\n"
        content += "url_poster:\n"
        content += "url_project:\n"
        content += "url_slides:\n"
        content += "url_source:\n"
        content += "url_video:\n\n"
        
        # 特色图片
        content += "# Featured image\n"
        content += "# To use, add an image named `featured.jpg/png` to your page's folder.\n"
        content += "# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.\n"
        content += "image:\n"
        content += '  caption: ""\n'
        content += '  focal_point: ""\n'
        content += "  preview_only: false\n\n"
        
        # 关联项目
        content += "# Associated Projects (optional).\n"
        content += "#   Associate this publication with one or more of your projects.\n"
        content += "#   Simply enter your project's folder or file name without extension.\n"
        content += "#   E.g. `internal-project` references `content/project/internal-project/index.md`.\n"
        content += "#   Otherwise, set `projects: []`.\n"
        content += "projects: []\n\n"
        
        # 幻灯片
        content += "# Slides (optional).\n"
        content += "#   Associate this publication with Markdown slides.\n"
        content += "#   Simply enter your slide deck's filename without extension.\n"
        content += "#   E.g. `slides: \"example\"` references `content/slides/example/index.md`.\n"
        content += "#   Otherwise, set `slides: \"\"`.\n"
        content += 'slides: ""\n'
        content += "---\n\n"
        
        return content
    
    def download_featured_image(self, paper_info: Dict, output_folder: Path) -> bool:
        """尝试下载论文的特色图片"""
        # 这里可以扩展，尝试从论文PDF或其他来源提取图片
        # 目前返回False，表示没有下载图片
        return False
    
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
            bibtex_content = self.create_bibtex(paper_info)
            bib_file = output_folder / "featured.bib"
            with open(bib_file, 'w', encoding='utf-8') as f:
                f.write(bibtex_content)
            
            # 尝试下载特色图片
            self.download_featured_image(paper_info, output_folder)
            
            print(f"✓ 成功创建论文文件夹: {output_folder}")
            print(f"  - index.md: Hugo内容文件")
            print(f"  - featured.bib: BibTeX引用文件")
            
            # 显示论文信息摘要
            print(f"\n论文信息摘要:")
            print(f"  标题: {paper_info.get('title', 'N/A')}")
            print(f"  作者: {', '.join(paper_info.get('authors', []))}")
            print(f"  发表: {paper_info.get('journal') or paper_info.get('venue', 'N/A')}")
            print(f"  年份: {paper_info.get('date', paper_info.get('year', 'N/A'))}")
            print(f"  来源: {', '.join(paper_info.get('sources', []))}")
            
            return True
            
        except Exception as e:
            print(f"创建文件夹失败: {e}")
            return False


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='论文信息爬虫和Hugo内容生成器')
    parser.add_argument('title', nargs='?', help='论文标题')
    parser.add_argument('--interactive', '-i', action='store_true', help='交互模式')
    parser.add_argument('--output-dir', '-o', default='content/publications', 
                       help='输出目录 (默认: content/publications)')
    
    args = parser.parse_args()
    
    crawler = PaperCrawler(args.output_dir)
    
    if args.interactive or not args.title:
        print("=== 论文信息爬虫 ===")
        print("输入论文标题来搜索和生成Hugo内容")
        print("输入 'quit' 或 'exit' 退出")
        print()
        
        while True:
            title = input("请输入论文标题: ").strip()
            if title.lower() in ['quit', 'exit', 'q']:
                break
            
            if not title:
                print("请输入有效的论文标题")
                continue
            
            print()
            paper_info = crawler.search_paper(title)
            
            if paper_info:
                print()
                success = crawler.create_paper_folder(paper_info)
                if success:
                    print("✓ 操作完成!")
                else:
                    print("✗ 操作失败!")
            else:
                print("✗ 未找到论文信息")
            
            print("\n" + "="*50 + "\n")
    
    else:
        # 单次运行模式
        paper_info = crawler.search_paper(args.title)
        
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
            sys.exit(1)


if __name__ == "__main__":
    main()
