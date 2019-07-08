---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Adaptively Exploring Population Mobility Patterns in Flow Visualization"
authors:
  [
    Fei Wang,
    Wei Chen,
    Ye Zhao,
    Tianyu Gu,
    Siyuan Gao,
    Hujun Bao,
  ]
date: 2017-08
doi: "10.1109/TITS.2017.2711644"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Intelligent Transportation Systems"
publication_short: "IEEE TITS"

abstract: "Thanks to the ubiquitous cell phone use, we have never been so close to uncover population mobility patterns in urban area. While some researches utilize cellphone call records to mine population patterns, few works aim to depict population movement in adaptively spatial and temporal representations, i.e., from a community, a district in the city over an hour, a day to a week. In this paper, we construct a system which deciphers, transforms, queries, and visualizes the records from the millions of users in a city. In particular, we design a data structure, namely MobiHash, which collects phone call records over base stations and indexes them by utilizing a Voronoi division of the urban space. MobiHash supports responsive data queries so that users can interactively retrieve trajectories reflecting population flows in areas of interest. Moreover, population movement is represented as vector fields to reduce visual clutter and occlusions. Because of sparse moving points, a novel radiation model is proposed to interpolate population passing zones. Case studies and experts' feedback validate the utility and efficiency by comparing population moving patterns in different times by using our system."

# Summary. An optional shortened abstract.
summary: ""

tags: ["Population Mobility Pattern", "Visual Query", "Flow Visualization", "Cell Phone Data"]
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
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/Adaptively%20Exploring%20Population%20Mobility%20Patterns%20in%20Flow%20Visualization.pdf
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