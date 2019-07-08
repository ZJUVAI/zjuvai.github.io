---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "LDSScanner: Exploratory Analysis of Low-Dimensional Structures in High-Dimensional Datasets"
authors:
  [
    Jiazhi Xia,
    Fenjin Ye,
    Wei Chen,
    Yusi Wang,
    Weifeng Chen,
    Yuxin Ma,
    Anthony K.H. Tung,
  ]
date: 2018-01
doi: "10.1109/TVCG.2017.2744098"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Visualization and Computer Graphics"
publication_short: "IEEE TVCG"

abstract: "Many approaches for analyzing a high-dimensional dataset assume that the dataset contains specific structures, e.g., clusters in linear subspaces or non-linear manifolds. This yields a trial-and-error process to verify the appropriate model and parameters. This paper contributes an exploratory interface that supports visual identification of low-dimensional structures in a high-dimensional dataset, and facilitates the optimized selection of data models and configurations. Our key idea is to abstract a set of global and local feature descriptors from the neighborhood graph-based representation of the latent low-dimensional structure, such as pairwise geodesic distance (GD) among points and pairwise local tangent space divergence (LTSD) among pointwise local tangent spaces (LTS). We propose a new LTSD-GD view, which is constructed by mapping LTSD and GD to the x axis and y axis using 1D multidimensional scaling, respectively. Unlike traditional dimensionality reduction methods that preserve various kinds of distances among points, the LTSD-GD view presents the distribution of pointwise LTS (x axis) and the variation of LTS in structures (the combination of x axis and y axis). We design and implement a suite of visual tools for navigating and reasoning about intrinsic structures of a high-dimensional dataset. Three case studies verify the effectiveness of our approach."

# Summary. An optional shortened abstract.
summary: ""

tags: ["High-dimensional data", "low-dimensional structure", "subspace", "manifold", "visual exploration"]
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
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/LDSScanner.pdf
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
  - https://vimeo.com/238313004

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