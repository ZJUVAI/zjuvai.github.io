#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
论文爬虫工具测试脚本
"""

import os
import sys
import shutil
from pathlib import Path

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from paper_crawler import PaperCrawler
    print("✓ 完整版爬虫可用")
    use_full_version = True
except ImportError as e:
    print(f"✗ 完整版爬虫不可用: {e}")
    try:
        from simple_paper_crawler import SimplePaperCrawler
        print("✓ 简化版爬虫可用")
        use_full_version = False
    except ImportError as e:
        print(f"✗ 简化版爬虫也不可用: {e}")
        sys.exit(1)


def test_paper_search():
    """测试论文搜索功能"""
    print("\n=== 测试论文搜索功能 ===")
    
    # 测试用例
    test_papers = [
        "ECharts: A Declarative Framework for Rapid Construction of Web-based Visualization",
        "D3.js",
        "Neural Networks for Machine Learning"
    ]
    
    # 创建测试输出目录
    test_output_dir = "test_publications"
    if Path(test_output_dir).exists():
        shutil.rmtree(test_output_dir)
    
    if use_full_version:
        crawler = PaperCrawler(test_output_dir)
    else:
        crawler = SimplePaperCrawler(test_output_dir)
    
    success_count = 0
    
    for i, title in enumerate(test_papers, 1):
        print(f"\n--- 测试 {i}/{len(test_papers)}: {title} ---")
        
        try:
            paper_info = crawler.search_paper(title)
            
            if paper_info:
                print(f"✓ 搜索成功")
                print(f"  标题: {paper_info.get('title', 'N/A')}")
                print(f"  作者数: {len(paper_info.get('authors', []))}")
                print(f"  摘要长度: {len(paper_info.get('abstract', ''))}")
                
                # 尝试创建文件夹
                success = crawler.create_paper_folder(paper_info)
                if success:
                    print(f"✓ 文件夹创建成功")
                    success_count += 1
                else:
                    print(f"✗ 文件夹创建失败")
            else:
                print(f"✗ 搜索失败")
        
        except Exception as e:
            print(f"✗ 测试出错: {e}")
    
    print(f"\n=== 测试结果 ===")
    print(f"成功: {success_count}/{len(test_papers)}")
    
    # 显示生成的文件
    if Path(test_output_dir).exists():
        print(f"\n生成的文件夹:")
        for folder in Path(test_output_dir).iterdir():
            if folder.is_dir():
                print(f"  📁 {folder.name}")
                for file in folder.iterdir():
                    print(f"    📄 {file.name}")
    
    return success_count > 0


def test_file_generation():
    """测试文件生成功能"""
    print("\n=== 测试文件生成功能 ===")
    
    # 模拟论文信息
    mock_paper_info = {
        'title': 'Test Paper: A Mock Example for Testing',
        'authors': ['John Doe', 'Jane Smith', 'Bob Johnson'],
        'abstract': 'This is a test abstract for testing purposes. It contains some mock content to verify that the file generation works correctly.',
        'date': '2024-01-15',
        'journal': 'Test Journal',
        'doi': '10.1234/test.2024.001',
        'url': 'https://example.com/test-paper',
        'fields': ['Computer Science', 'Testing', 'Software Engineering'],
        'source': 'test'
    }
    
    test_output_dir = "test_publications"
    
    if use_full_version:
        crawler = PaperCrawler(test_output_dir)
    else:
        crawler = SimplePaperCrawler(test_output_dir)
    
    try:
        success = crawler.create_paper_folder(mock_paper_info)
        
        if success:
            print("✓ 文件生成测试成功")
            
            # 检查生成的文件
            folder_name = crawler.generate_folder_name(mock_paper_info)
            folder_path = Path(test_output_dir) / folder_name
            
            index_file = folder_path / "index.md"
            bib_file = folder_path / "featured.bib"
            
            if index_file.exists():
                print("✓ index.md 文件已生成")
                with open(index_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'Test Paper: A Mock Example for Testing' in content:
                        print("✓ index.md 内容正确")
                    else:
                        print("✗ index.md 内容有误")
            else:
                print("✗ index.md 文件未生成")
            
            if bib_file.exists():
                print("✓ featured.bib 文件已生成")
                with open(bib_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'Test Paper: A Mock Example for Testing' in content:
                        print("✓ featured.bib 内容正确")
                    else:
                        print("✗ featured.bib 内容有误")
            else:
                print("✗ featured.bib 文件未生成")
            
            return True
        else:
            print("✗ 文件生成测试失败")
            return False
    
    except Exception as e:
        print(f"✗ 文件生成测试出错: {e}")
        return False


def main():
    """主测试函数"""
    print("=== 论文爬虫工具测试 ===")
    print(f"使用版本: {'完整版' if use_full_version else '简化版'}")
    
    # 运行测试
    search_success = test_paper_search()
    file_success = test_file_generation()
    
    print(f"\n=== 总体测试结果 ===")
    if search_success and file_success:
        print("✓ 所有测试通过")
        print("\n工具已准备就绪，可以开始使用！")
        print("\n使用方法:")
        if use_full_version:
            print("  python paper_crawler.py --interactive")
            print("  或")
            print("  paper_crawler.bat")
        else:
            print("  python simple_paper_crawler.py \"论文标题\"")
    else:
        print("✗ 部分测试失败")
        print("请检查网络连接和依赖安装")
    
    # 清理测试文件
    test_output_dir = "test_publications"
    if Path(test_output_dir).exists():
        try:
            shutil.rmtree(test_output_dir)
            print(f"\n✓ 清理测试文件完成")
        except Exception as e:
            print(f"\n警告: 清理测试文件失败: {e}")


if __name__ == "__main__":
    main()
