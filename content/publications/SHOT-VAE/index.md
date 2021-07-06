---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "SHOT-VAE: Semi-supervised Deep Generative Models With Label-aware ELBO Approximations"
authors: [Haozhe Feng,Kezhi Kong, Minghao Chen, Tianye Zhang, Minfeng Zhu,  Wei Chen]
date: 2021-05-18
doi: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Proceedings of the AAAI Conference on Artificial Intelligence"
publication_short: "AAAI"

abstract: "Semi-supervised variational autoencoders (VAEs) have obtained strong results, but have also encountered the challenge that good ELBO values do not always imply accurate inference results.In this paper, we investigate and propose two causes of this problem: (1) The ELBO objective cannot utilize the label information directly. (2) A bottleneck value exists, and continuing to optimize ELBO after this value will not improve inference accuracy. On the basis of the experiment results, we propose SHOT-VAE to address these problems without introducing additional prior knowledge. The SHOT-VAE offers two contributions: (1) A new ELBO approximation named smooth-ELBO that integrates the label predictive loss into ELBO. (2) An approximation based on optimal interpolation that breaks the ELBO value bottleneck by reducing the margin between ELBO and the data likelihood. The SHOT-VAE achieves good performance with 25.30% error rate on CIFAR-100 with 10k labels and reduces the error rate to 6.11% on CIFAR-10 with 4k labels."

# Summary. An optional shortened abstract.
summary: ""

tags:
  [
    "Node-link diagram",
    "graph layout",
    "graph visualization",
	  "user interactions",
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
  - https://ojs.aaai.org/index.php/AAAI/article/download/16909/16716
url_code: 
  - https://github.com/FengHZ/AAAI2021-260
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
url_supp:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "featured"
  focal_point: "Center"
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
