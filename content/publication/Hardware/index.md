---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Hardware Accelerated Adaptive EWA Volume Splatting"
authors:
  [ Wei Chen, Liu Ren, Matthias Zwicker, Hanspter Pfister ]
date: 2004-10-10
doi: "https://doi.org/10.1109/VISUAL.2004.38"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Visualization"
publication_short: ""

abstract: "We present a hardware-accelerated adaptive EWA (elliptical weighted average) volume splatting algorithm. EWA splatting combines a Gaussian reconstruction kernel with a low-pass image filter for high image quality without aliasing artifacts or excessive blurring. We introduce a novel adaptive filtering scheme to reduce the computational cost of EWA splatting. We show how this algorithm can be efficiently implemented on modern graphics processing units (GPUs). Our implementation includes interactive classification and fast lighting. To accelerate the rendering we store splat geometry and 3D volume data locally in GPU memory. We present results for several rectilinear volume datasets that demonstrate the high image quality and interactive rendering speed of our method."

# Summary. An optional shortened abstract.
summary: ""

tags:
  [
	"Direct volume rendering", "volume splatting", "EWA filter", "hardware acceleration"
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
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/IEEEVis2004/paper279.pdf
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/IEEEVis2004/part1_high.mov
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/IEEEVis2004/part2_high.mov

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
