---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Efficient Volume Exploration Using the Gaussian Mixture Model."
authors:
  [
    Yunhai Wang,
    Wei Chen,
    Jian Zhang,
    Tingxing Dong,
    Guihua Shan,
    Xuebin Chi,
  ]
date: 2018-06-01T08:00:00+08:00
doi: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Visualization and Computer Graphics"
publication_short: "IEEE TVCG"

abstract: "The multidimensional transfer function is a flexible and effective tool for exploring volume data. However, designing an appropriate transfer function is a trial-and-error process and remains a challenge. In this paper, we propose a novel volume exploration scheme that explores volumetric structures in the feature space by modeling the space using the Gaussian mixture model (GMM). Our new approach has three distinctive advantages. First, an initial feature separation can be automatically achieved through GMM estimation. Second, the calculated Gaussians can be directly mapped to a set of elliptical transfer functions (ETFs), facilitating a fast pre-integrated volume rendering process. Third, an inexperienced user can flexibly manipulate the ETFs with the assistance of a suite of simple widgets, and discover potential features with several interactions. We further extend the GMM-based exploration scheme to time-varying data sets using an incremental GMM estimation algorithm. The algorithm estimates the GMM for one time step by using itself and the GMM generated from its previous steps. Sequentially applying the incremental algorithm to all time steps in a selected time interval yields a preliminary classification for each time step. In addition, the computed ETFs can be freely adjusted. The adjustments are then automatically propagated to other time steps. In this way, coherent user-guided exploration of a given time interval is achieved. Our GPU implementation demonstrates interactive performance and good scalability. The effectiveness of our approach is verified on several data sets."

# Summary. An optional shortened abstract.
summary: ""

tags:
  ["Volume classification", "volume rendering", "Gaussian mixture model", "time-varying data","temporal coherence"]
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
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/IEEETVCG2011_Wangyunhai/gmm_2011.pdf
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/IEEETVCG2011_Wangyunhai/GMM.avi
  

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
