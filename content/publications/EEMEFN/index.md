---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "EEMEFN: Low-Light Image Enhancement via Edge-Enhanced Multi-Exposure Fusion Network"
authors: [Minfeng Zhu, Pingbo Pan, Wei Chen, Yi Yang]
date: 2019-11-26
doi: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Proceedings of the 34th AAAI Conference on Artificial Intelligence"
publication_short: "AAAI"

abstract: "This work focuses on the extremely low-light image enhance-ment, which aims to improve image brightness and revealhidden information in darken areas. Recently, image enhance-ment approaches have yielded impressive progress. However,existing methods still suffer from three main problems: (1)low-light images usually are high-contrast. Existing methodsmay fail to recover images details in extremely dark or brightareas; (2) current methods cannot precisely correct the colorof low-light images; (3) when the object edges are unclear,the pixel-wise loss may treat pixels of different objectsequally and produce blurry images. In this paper, we proposea two-stage method called Edge-Enhanced Multi-ExposureFusion Network (EEMEFN) to enhance extremely low-lightimages. In the first stage, we employ a multi-exposure fusionmodule to address the high contrast and color bias issues. Wesynthesize a set of images with different exposure time froma single image and construct an accurate normal-light imageby combining well-exposed areas under different illuminationconditions. Thus, it can produce realistic initial images withcorrect color from extremely noisy and low-light images.Secondly, we introduce an edge enhancement module torefine the initial images with the help of the edge information.Therefore, our method can reconstruct high-quality imageswith sharp edges when minimizing the pixel-wise loss. Ex-periments on the See-in-the-Dark dataset indicate that ourEEMEFN approach achieves state-of-the-art performance."

# Summary. An optional shortened abstract.
summary: ""

tags: []
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
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/EEMEFN-Low%20Light%20Image%20Enhancement%20via%20Edge%20Enhanced%20MultiExposure%20Fusion%20Network.pdf
url_code:
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
