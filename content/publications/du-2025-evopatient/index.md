---

title: "LLMs Can Simulate Standardized Patients via Agent Coevolution"
authors: [Zhuoyun Du, Lujie Zheng, Renjun Hu, Yuyang Xu, Xiawei Li, Ying Sun, Wei Chen, Jian Wu, Haolei Cai, Haochao Ying]
date: 2025-07-01
doi: "10.18653/v1/2025.acl-long.846"

# Publication type.
# Legend: 0 = Uncategorized, 1 = Conference paper, 2 = Journal article,
# 3 = Preprint / Working Paper, 4 = Report, 5 = Book, 6 = Book section,
# 7 = Thesis, 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "The 63rd Annual Meeting of the Association for Computational Linguistics"
publication_short: "ACL"

abstract: "Training medical personnel using standardized patients (SPs) remains a complex challenge, requiring extensive domain expertise and role-specific practice. Most research on Large Language Model (LLM)-based simulated patients focuses on improving data retrieval accuracy or adjusting prompts through human feedback. However, this focus has overlooked the critical need for patient agents to learn a standardized presentation pattern that transforms data into human-like patient responses through unsupervised simulations. To address this gap, we propose EvoPatient, a novel simulated patient framework in which a patient agent and doctor agents simulate the diagnostic process through multi-turn dialogues, simultaneously gathering experience to improve the quality of both questions and answers, ultimately enabling human doctor training. Extensive experiments on various cases demonstrate that, by providing only overall SP requirements, our framework improves over existing reasoning methods by more than 10% in requirement alignment and better human preference, while achieving an optimal balance of resource consumption after evolving over 200 cases for 10 hours, with excellent generalizability."

# Summary. An optional shortened abstract.
summary: ""

tags:
  ["Large Language Models", "Medical Training", "Agent Simulation", "Dialogue Systems"]
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
 - "https://aclanthology.org/2025.acl-long.846.pdf"
url_code: 
 - "https://github.com/ZJUMAI/EvoPatient"
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
