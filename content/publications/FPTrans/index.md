---

title: "Feature-Proxy Transformer for Few-Shot Segmentation"
authors: [Jianwei Zhang, Yifan Sun, Yi Yang, Wei Chen]
date: 2022-11-01
doi: "10.48550/arXiv.2210.06908"

# Publication type.
# Legend: 0 = Uncategorized, 1 = Conference paper, 2 = Journal article,
# 3 = Preprint / Working Paper, 4 = Report, 5 = Book, 6 = Book section,
# 7 = Thesis, 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Proceedings of the Advances in Neural Information Processing Systems"
publication_short: "NeurIPS"

abstract: "Few-shot segmentation~(FSS) aims at performing semantic segmentation on novel classes given a few annotated support samples. With a rethink of recent advances, we find that the current FSS framework has deviated far from the supervised segmentation framework: Given the deep features, FSS methods typically use an intricate decoder to perform sophisticated pixel-wise matching, while the supervised segmentation methods use a simple linear classification head. Due to the intricacy of the decoder and its matching pipeline, it is not easy to follow such an FSS framework. This paper revives the straightforward framework of \"feature extractor linear classification head\" and proposes a novel Feature-Proxy Transformer (FPTrans) method, in which the \"proxy\" is the vector representing a semantic class in the linear classification head. FPTrans has two keypoints for learning discriminative features and representative proxies: 1) To better utilize the limited support samples, the feature extractor makes the query interact with the support features from bottom to top layers using a novel prompting strategy. 2) FPTrans uses multiple local background proxies (instead of a single one) because the background is not homogeneous and may contain some novel foreground regions. These two keypoints are easily integrated into the vision transformer backbone with the prompting mechanism in the transformer. Given the learned features and proxies, FPTrans directly compares their cosine similarity for segmentation. Although the framework is straightforward, we show that FPTrans achieves competitive FSS accuracy on par with state-of-the-art decoder-based methods."

# Summary. An optional shortened abstract.
summary: ""

tags:
  [
    "few-shot segmentation", 
    "vision transformer", 
    "prompt learning"
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
  - https://openreview.net/pdf?id=hBaI5MY0CBz
url_code:
  - https://github.com/Jarvis73/FPTrans
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