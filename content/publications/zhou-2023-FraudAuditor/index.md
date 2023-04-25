---

title: "FraudAuditor: A Visual Analytics Approach for Collusive Fraud in Health Insurance"
authors: [Jiehui Zhou, Xumeng Wang, Jie Wang, Hui Ye, Huanliang Wang, Zihan Zhou, Dongming Han, Haochao Ying, Jian Wu, Wei Chen]
date: 2023-03-27
doi: "10.1109/TVCG.2023.3261910"

# Publication type.
# Legend: 0 = Uncategorized, 1 = Conference paper, 2 = Journal article,
# 3 = Preprint / Working Paper, 4 = Report, 5 = Book, 6 = Book section,
# 7 = Thesis, 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Visualization and Computer Graphics"
publication_short: "IEEE TVCG"

abstract: "Collusive fraud, in which multiple fraudsters collude to defraud health insurance funds, threatens the operation of the healthcare system. However, existing statistical and machine learning-based methods have limited ability to detect fraud in the scenario of health insurance due to the high similarity of fraudulent behaviors to normal medical visits and the lack of labeled data. To ensure the accuracy of the detection results, expert knowledge needs to be integrated with the fraud detection process. By working closely with health insurance audit experts, we propose FraudAuditor, a three-stage visual analytics approach to collusive fraud detection in health insurance. Specifically, we first allow users to interactively construct a co-visit network to holistically model the visit relationships of different patients. Second, an improved community detection algorithm that considers the strength of fraud likelihood is designed to detect suspicious fraudulent groups. Finally, through our visual interface, users can compare, investigate, and verify suspicious patient behavior with tailored visualizations that support different time scales. We conducted case studies in a real-world healthcare scenario, i.e., to help locate the actual fraud group and exclude the false positive group. The results and expert feedback proved the effectiveness and usability of the approach."

# Summary. An optional shortened abstract.
summary: ""

tags:
  [
    "collusive fraud", 
    "fraud detection", 
    "health insurance", 
    "visual analytics"
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
  - https://arxiv.org/pdf/2303.13491.pdf
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
  - https://www.youtube.com/watch?v=PlCQhtpYylQ
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