# 论文信息爬虫工具

这是一个自动爬取论文信息并为Hugo网站生成相应content结构的工具。

## 功能特性

- 🔍 **多数据源搜索**: 支持从以下数据源搜索论文信息：
  - Semantic Scholar (语义学者)
  - arXiv
  - Crossref
  - DBLP
- 📄 **自动生成Hugo内容**: 根据论文信息生成完整的Hugo网站内容结构
- 📚 **BibTeX引用生成**: 自动生成规范的BibTeX引用文件
- 🎨 **智能信息合并**: 智能合并多个数据源的信息，提供最完整的论文信息
- 💻 **跨平台支持**: 支持Windows、macOS和Linux

## 安装要求

### Python环境
- Python 3.6 或更高版本
- pip包管理器

### 依赖包
```bash
pip install -r requirements.txt
```

主要依赖：
- `requests`: HTTP请求库
- `bibtexparser`: BibTeX解析和生成库

## 使用方法

### 方法1: 批处理脚本 (Windows推荐)

```bash
# 交互模式
paper_crawler.bat

# 直接搜索
paper_crawler.bat "ECharts: A Declarative Framework for Rapid Construction of Web-based Visualization"
```

### 方法2: Python脚本

```bash
# 交互模式
python paper_crawler.py --interactive

# 直接搜索
python paper_crawler.py "论文标题"

# 指定输出目录
python paper_crawler.py "论文标题" --output-dir custom/path
```

## 使用示例

### 交互模式示例
```
=== 论文信息爬虫 ===
输入论文标题来搜索和生成Hugo内容
输入 'quit' 或 'exit' 退出

请输入论文标题: ECharts: A Declarative Framework for Rapid Construction of Web-based Visualization

正在搜索论文: ECharts: A Declarative Framework for Rapid Construction of Web-based Visualization
  - 搜索 Semantic Scholar...
    ✓ 找到结果
  - 搜索 arXiv...
    ✗ 未找到结果
  - 搜索 Crossref...
    ✓ 找到结果
  - 搜索 DBLP...
    ✓ 找到结果
  ✓ 成功合并来自 3 个数据源的信息

✓ 成功创建论文文件夹: content/publications/ECharts A Declarative Framework for Rapid Construction of Web-based Visualization
  - index.md: Hugo内容文件
  - featured.bib: BibTeX引用文件

论文信息摘要:
  标题: ECharts: A Declarative Framework for Rapid Construction of Web-based Visualization
  作者: Deqing Li, Honghui Mei, Yi Shen, Shuang Su, Wenli Zhang, Junting Wang, Ming Zu, Wei Chen
  发表: Visual Informatics
  年份: 2018-06-01
  来源: semantic_scholar, crossref, dblp
✓ 操作完成!
```

### 生成的文件结构
```
content/publications/[论文标题]/
├── index.md          # Hugo前言配置文件
├── featured.bib      # BibTeX引用文件
└── featured.png      # 特色图片（如果可用）
```

## 配置选项

### 命令行参数
- `title`: 论文标题（位置参数）
- `--interactive`, `-i`: 启动交互模式
- `--output-dir`, `-o`: 指定输出目录（默认: content/publications）

### 自定义输出目录
```bash
python paper_crawler.py "论文标题" --output-dir "custom/publications"
```

## 生成内容说明

### index.md文件
包含Hugo网站所需的前言配置：
- 论文标题、作者、摘要
- 发表信息（期刊/会议、日期）
- DOI和URL链接
- 发表类型分类
- 标签和分类
- 各种链接字段（PDF、代码、数据集等）

### featured.bib文件
标准的BibTeX引用格式，包含：
- 完整的引用信息
- DOI和URL
- 摘要信息

## 数据源说明

### Semantic Scholar
- **优势**: 信息最全面，包含引用计数、研究领域等
- **覆盖范围**: 计算机科学、生物医学等多个领域
- **限制**: 部分论文可能没有收录

### arXiv
- **优势**: 最新的预印本论文，更新及时
- **覆盖范围**: 物理、数学、计算机科学、生物学等
- **限制**: 主要是预印本，可能缺少正式发表信息

### Crossref
- **优势**: 权威的DOI数据库，信息准确
- **覆盖范围**: 大部分正式发表的学术论文
- **限制**: 主要是正式发表的论文，预印本较少

### DBLP
- **优势**: 计算机科学领域最权威的数据库
- **覆盖范围**: 计算机科学领域论文
- **限制**: 仅限计算机科学领域

## 常见问题

### Q: 搜索不到论文怎么办？
A: 
1. 检查论文标题是否正确
2. 尝试使用论文的英文标题
3. 简化标题，去掉副标题
4. 检查网络连接

### Q: 生成的信息不完整怎么办？
A: 
1. 工具会合并多个数据源的信息
2. 可以手动编辑生成的`index.md`文件
3. 不同数据源的信息完整程度不同

### Q: 文件夹已存在怎么办？
A: 工具会询问是否覆盖，选择'y'覆盖或'N'取消

### Q: 如何添加论文PDF或图片？
A: 
1. 将PDF文件放入论文文件夹，并在`index.md`中更新`url_pdf`字段
2. 将特色图片命名为`featured.jpg`或`featured.png`放入文件夹

## 扩展开发

### 添加新的数据源
在`PaperCrawler`类中添加新的搜索方法：
```python
def search_new_source(self, title: str) -> Optional[Dict]:
    # 实现新数据源的搜索逻辑
    pass
```

### 自定义输出格式
修改`create_hugo_content`方法来自定义生成的Hugo内容格式。

### 添加图片下载功能
扩展`download_featured_image`方法来从论文PDF或其他来源提取图片。

## 许可证
此工具遵循ISC许可证。

## 贡献
欢迎提交Issue和Pull Request来改进这个工具。

## 联系方式
如有问题或建议，请通过GitHub Issues联系。
