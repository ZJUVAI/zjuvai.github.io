---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Automatic Shader Simplification using Surface Signal Approximation."
authors:
  [
	Rui Wang,
    Hujun Bao,
    Karla Bala,
    Xianjin Yang,
    Yazhen Yuan,
    Wei Chen.,
  ]
date: 2014-11
doi: "10.1145/2661229.2661276"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "ACM Transactions on Graphics"
publication_short: "ACM TOG"

abstract: "In this paper, we present a new automatic shader simplification method using surface signal approximation. We regard the entire multi-stage rendering pipeline as a process that generates signals on surfaces, and we formulate the simplification of the fragment shader as a global simplification problem across multi-shader stages. Three new shader simplification rules are proposed to solve the problem. First, the code transformation rule transforms fragment shader code to other shader stages in order to redistribute computations on pixels up to the level of geometry primitives. Second, the surface-wise approximation rule uses high-order polynomial basis functions on surfaces to approximate pixel-wise computations in the fragment shader. These approximations are pre-cached and simplify computations at runtime. Third, the surface subdivision rule tessellates surfaces into smaller patches. It combines with the previous two rules to approximate pixel-wise signals at different levels of tessellations with different computation times and visual errors. To evaluate simplified shaders using these simplification rules, we introduce a new cost model that includes the visual quality, rendering time and memory consumption. With these simplification rules and the cost model, we present an integrated shader simplification algorithm that is capable of automatically generating variants of simplified shaders and selecting a sequence of preferable shaders. Results show that the sequence of selected simplified shaders balance performance, accuracy and memory consumption well."

# Summary. An optional shortened abstract.
summary: ""

tags: ["TGPU shader", "real-time rendering", "shader simplification", "surface signal approximation"]
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
  preview_only: fase

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
