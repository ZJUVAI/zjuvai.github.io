---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: 'SemanticTraj: A New Approach to Interacting with Massive Taxi Trajectories'
authors:
    [Shamal Al-Dohuki,
               Yingyu Wu,
               Farah Kamw,
               Jing Yang,
               Xin Li,
               Ye Zhao,
               Xinyue Ye,
               Wei Chen,
               Chao Ma,
               Fei Wang
    ]
date: 2016-08-25
doi: ''

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: 'IEEE Transactions on Visualization and Computer Graphics'
publication_short: 'IEEE TVCG'

abstract: 'Massive taxi trajectory data is exploited for knowledge discovery in transportation and urban planning. Existing tools typically require users to select and brush geospatial regions on a map when retrieving and exploring taxi trajectories and passenger trips. To answer seemingly simple questions such as “What were the taxi trips starting from Main Street and ending at Wall Street in the morning?” or “Where are the taxis arriving at the Art Museum at noon typically coming from?”, tedious and time consuming interactions are usually needed since the numeric GPS points of trajectories are not directly linked to the keywords such as “Main Street”, “Wall Street”, and “Art Museum”. In this paper, we present SemanticTraj, a new method for managing and visualizing taxi trajectory data in an intuitive, semantic rich, and efficient means. With SemanticTraj, domain and public users can find answers to the aforementioned questions easily through direct queries based on the terms. They can also interactively explore the retrieved data in visualizations enhanced by semantic information of the trajectories and trips. In particular, taxi trajectories are converted into taxi documents through a textualization transformation process. This process maps GPS points into a series of street/POI names and pick-up/drop-off locations. It also converts vehicle speeds into user-defined descriptive terms. Then, a corpus of taxi documents is formed and indexed to enable flexible semantic queries over a text search engine. Semantic labels and meta-summaries of the results are integrated with a set of visualizations in a SemanticTraj prototype, which helps users study taxi trajectories quickly and easily. A set of usage scenarios are presented to show the usability of the system. We also collected feedback from domain experts and conducted a preliminary user study to evaluate the visual system.'

# Summary. An optional shortened abstract.
summary: ''

tags:
    ['Semantic', 'Taxi', 'Trajectory', 'Question', 'Urban', 'Transportation','Search']
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
    - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/SemanticTraj.pdf
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
    # - able to add more videos

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
    caption: 'featured'
    focal_point: 'Top'
    preview_only: false
# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: ""
---
