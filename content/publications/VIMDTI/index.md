---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Volume Illustration of Muscle from Diffusion Tensor Images."
authors:
  [
    Wei Chen,
    Zhicheng Yan,
    Song Zhang,
    John Allen Crow,
    David S. Ebert,
    R. McLaughlin,
    K. Mullins,
    R. Cooper,
    Zi’ang Ding,
    Jun Liao,
  ]
date: 2009-1-11T17:20:04+08:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2009-06-29T17:20:04+08:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Visualization and Computer Graphics"
publication_short: "IEEE TVCG"

abstract: "Medical illustration has demonstrated its effectiveness to depict salient anatomical features while hiding the irrelevant details. Current solutions are ineffective for visualizing fibrous structures such as muscle, because typical datasets (CT or MRI) do not contain directional details. In this paper, we introduce a new muscle illustration approach that leverages diffusion tensor imaging (DTI) data and example-based texture synthesis techniques. Beginning with a volumetric diffusion tensor image, we reformulate it into a scalar field and an auxiliary guidance vector field to represent the structure and orientation of a muscle bundle. A muscle mask derived from the input diffusion tensor image is used to classify the muscle structure. The guidance vector field is further refined to remove noise and clarify structure. To simulate the internal appearance of the muscle, we propose a new two-dimensional examplebased solid texture synthesis algorithm that builds a solid texture constrained by the guidance vector field. Illustrating the constructed scalar field and solid texture efficiently highlights the global appearance of the muscle as well as the local shape and structure of the muscle fibers in an illustrative fashion. We have applied the proposed approach to five example datasets (four pig hearts and a pig leg), demonstrating plausible illustration and expressiveness."

# Summary. An optional shortened abstract.
summary: ""

tags:
  [
    "Illustrative Visualization",
    "Diffusion Tensor Image",
    "Muscle",
    "Solid Texture Synthesis",
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
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/IEEEVis2009/Vis2009_Printed_VolIll.pdf
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/IEEEVis2009/muscleModeling_xvid.avi

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
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
