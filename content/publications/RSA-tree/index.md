---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "RSATree: Distribution-AwareData Representation of Large-Scale Tabular Datasets for Flexible Visual Query"
authors: [Honghui Mei, Wei Chen, Yating Wei, Yuanzhe Hu, Shuyue Zhou, Bingru Lin, Ying Zhao, Jiazhi Xia]
date: 2019-08-06
doi: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "TVCG"
publication_short: "IEEE Transactions on Visualization and Computer Graphics"

abstract: "Analysts commonly investigate the data distributions derived from statistical aggregations of data that are represented by charts, such as histograms and binned scatterplots, to visualize and analyze a large-scale dataset. Aggregate queries are implicitly executed through such a process. Datasets are constantly extremely large; thus, the response time should be accelerated by calculating predefined data cubes. However, the queries are limited to the predefined binning schema of preprocessed data cubes. Such limitation hinders analysts' flexible adjustment of visual specifications to investigate the implicit patterns in the data effectively. Particularly, RSATree enables arbitrary queries and flexible binning strategies by leveraging three schemes, namely, an R-tree-based space partitioning scheme to catch the data distribution, a locality-sensitive hashing technique to achieve locality-preserving random access to data items, and a summed area table scheme to support interactive query of aggregated values with a linear computational complexity. This study presents and implements a web-based visual query system that supports visual specification, query, and exploration of large-scale tabular data with user-adjustable granularities. We demonstrate the efficiency and utility of our approach by performing various experiments on real-world datasets and analyzing time and space complexity."

# Summary. An optional shortened abstract.
summary: ""

tags:
  [
    "Aggregate query",
    "visual query",
    "large-scale data visualization",
    "R-tree",
    "summed area table",
	"hashing",
  ]
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/sat.pdf
url_code:
  - https://github.com/ZJUVAG/RSA_Tree
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "featured"
  focal_point: "Top"
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
