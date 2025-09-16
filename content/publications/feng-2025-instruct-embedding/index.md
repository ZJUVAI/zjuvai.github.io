---

title: "Don’t Reinvent the Wheel: Efficient Instruction-Following Text Embedding based on Guided Space Transformation"
authors: [Yingchaojie Feng, Yiqun Sun, Yandong Wen, Minfeng Zhu, Qiang Huang, Anthony Kum Hoe Tung, Wei Chen]
date: 2025-07-01
doi: "10.18653/v1/2025.acl-long.1196"

# Publication type.
# Legend: 0 = Uncategorized, 1 = Conference paper, 2 = Journal article,
# 3 = Preprint / Working Paper, 4 = Report, 5 = Book, 6 = Book section,
# 7 = Thesis, 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "The 63rd Annual Meeting of the Association for Computational Linguistics"
publication_short: "ACL"

abstract: "In this work, we investigate an important task named instruction-following text embedding, which generates dynamic text embeddings that adapt to user instructions, highlighting specific attributes of text. Despite recent advancements, existing approaches suffer from significant computational overhead, as they require re-encoding the entire corpus for each new instruction. To address this challenge, we propose GSTransform, a novel instruction-following text embedding framework based on Guided Space Transformation. Our key observation is that instruction-relevant information is inherently encoded in generic embeddings but remains underutilized. Instead of repeatedly encoding the corpus for each instruction, GSTransform is a lightweight transformation mechanism that adapts pre-computed embeddings in real time to align with user instructions, guided by a small amount of text data with instruction-focused label annotation. We conduct extensive experiments on three instruction-awareness downstream tasks across nine real-world datasets, demonstrating that GSTransform improves instruction-following text embedding quality over state-of-the-art methods while achieving dramatic speedups of 6~300× in real-time processing on large-scale datasets."

# Summary. An optional shortened abstract.
summary: ""

tags:
  ["Natural Language Processing", "Text Embedding", "Instruction Following", "Representation Learning"]
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
 - "https://aclanthology.org/2025.acl-long.1196.pdf"
url_code: 
 - "https://github.com/YingchaojieFeng/GSTransform"
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
