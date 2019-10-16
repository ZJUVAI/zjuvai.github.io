---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Semantics-Space-Time Cube: A Conceptual Framework for Systematic Analysis of Texts in Space and Time."
authors: [Jie Li, Siming Chen, Wei Chen, Gennady Andrienko, Natalia Andrienko]
date: 2018-11-20
doi: "10.1109/TVCG.2018.2882449"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Visualization and Computer Graphics"
publication_short: "IEEE TVCG"

abstract: "We propose an approach to analyzing data in which texts are associated with spatial and temporal references with the aim to understand how the text semantics vary over space and time. To represent the semantics, we apply probabilistic topic modeling. After extracting a set of topics and representing the texts by vectors of topic weights, we aggregate the data into a data cube with the dimensions corresponding to the set of topics, the set of spatial locations (e.g., regions), and the time divided into suitable intervals according to the scale of the planned analysis. Each cube cell corresponds to a combination (topic, location, time interval) and contains aggregate measures characterizing the subset of the texts concerning this topic and having the spatial and temporal references within these location and interval. Based on this structure, we systematically describe the space of analysis tasks on exploring the interrelationships among the three heterogeneous information facets, semantics, space, and time. We introduce the operations of projecting and slicing the cube, which are used to decompose complex tasks into simpler subtasks. We then present a design of a visual analytics system intended to support these subtasks. To reduce the complexity of the user interface, we apply the principles of structural, visual, and operational uniformity while respecting the specific properties of each facet. The aggregated data are represented in three parallel views corresponding to the three facets and providing different complementary perspectives on the data. The views have similar look-and-feel to the extent allowed by the facet specifics. Uniform interactive operations applicable to any view support establishing links between the facets. The uniformity principle is also applied in supporting the projecting and slicing operations on the data cube. We evaluate the feasibility and utility of the approach by applying it in two analysis scenarios using geolocated social media data for studying people's reactions to social and natural events of different spatial and temporal scales."

# Summary. An optional shortened abstract.
summary: ""

tags:
  [
    "spatiotemporal visualization",
    "semantic visualization",
    "data cube",
    "interactive exploration",
    "visual analytics",
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
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/Semantics-Space-Time%20Cube.pdf
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
