---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Structuring Feature Space: A Non-Parametric Method for Volumetric Transfer Function Generation."
authors: [Ross Maciejewski, Insoo Wu, Wei Chen, David S. Ebert]
date: 2009-11-01
doi: "10.1109/TVCG.2009.185"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Visualization and Computer Graphics"
publication_short: "IEEE TVCG"

abstract: "The use of multi-dimensional transfer functions for direct volume rendering has been shown to be an effective means of extracting materials and their boundaries for both scalar and multivariate data. The most common multi-dimensional transfer function consists of a two-dimensional (2D) histogram with axes representing a subset of the feature space (e.g., value vs. value gradient magnitude), with each entry in the 2D histogram being the number of voxels at a given feature space pair. Users then assign color and opacity to the voxel distributions within the given feature space through the use of interactive widgets (e.g., box, circular, triangular selection). Unfortunately, such tools lead users through a trial-and-error approach as they assess which data values within the feature space map to a given area of interest within the volumetric space. In this work, we propose the addition of non-parametric clustering within the transfer function feature space in order to extract patterns and guide transfer function generation. We apply a non-parametric kernel density estimation to group voxels of similar features within the 2D histogram. These groups are then binned and colored based on their estimated density, and the user may interactively grow and shrink the binned regions to explore feature boundaries and extract regions of interest. We also extend this scheme to temporal volumetric data in which time steps of 2D histograms are composited into a histogram volume. A three-dimensional (3D) density estimation is then applied, and users can explore regions within the feature space across time without adjusting the transfer function at each time step. Our work enables users to effectively explore the structures found within a feature space of the volume and provide a context in which the user can understand how these structures relate to their volumetric data. We provide tools for enhanced exploration and manipulation of the transfer function, and we show that the initial transfer function generation serves as a reasonable base for volumetric rendering, reducing the trial-and-error overhead typically found in transfer function design."

# Summary. An optional shortened abstract.
summary: ""

tags:
  [
    "Volume rendering",
    "kernel density estimation",
    "transfer function design",
    "temporal volume rendering",
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
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/IEEEVis2009/Vis09_Features.pdf
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/IEEEVis2009/kdefeet.WMV

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
