---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Image-Space Texture-Based Output-Coherent Surface Flow Visualization."
authors:
  [
    Jin Huang,
    Zherong Pan,
    Guoning Chen,
    Wei Chen,
    Hujun Bao,
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
publication_short: "VIEEE TVCG"

abstract: "Image-space line integral convolution (LIC) is a popular scheme for visualizing surface vector fields due to its simplicity and high efficiency. To avoid inconsistencies or color blur during the user interactions, existing approaches employ surface parameterization or 3D volume texture schemes. However, they often require expensive computation or memory cost, and cannot achieve consistent results in terms of both the granularity and color distribution on different scales. This paper introduces a novel image-space surface flow visualization approach that preserves the coherence during user interactions. To make the noise texture under different viewpoints coherent, we propose to precompute a sequence of mipmap noise textures in a coarse-to-fine manner for consistent transition, and map the textures onto each triangle with randomly assigned and constant texture coordinates. Further, a standard image-space LIC is performed to generate the flow texture. The proposed approach is simple and GPU-friendly, and can be easily combined with various texture-based flow visualization techniques. By leveraging viewpoint-dependent backward tracing and mipmap noise phase, our method can be incorporated with the image-based flow visualization (IBFV) technique for coherent visualization of unsteady flows. We demonstrate consistent and highly efficient flow visualization on a variety of data sets."

# Summary. An optional shortened abstract.
summary: ""

tags:
  ["Flow visualization", "mipmap", "LIC", "IBFV", "surface flows", "unsteady flows"]
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
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/IEEETVCG_huangjin/tvcgsi-2012-05-0092-1-compress.pdf
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
