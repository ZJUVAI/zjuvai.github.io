---

title: "Visual Diagnostics of Parallel Performance in Training Large-Scale DNN Models"
authors: [Yating Wei, Zhiyong Wang, Zhongwei Wang, Yong Dai, Gongchang Ou, Han Gao, Haitao Yang, Yue Wang, Caleb Chen Cao, Luoxuan Weng, Jiaying Lu, Rongchen Zhu, Wei Chen]
date: 2023-02-09
doi: "10.1109/TVCG.2023.3243228"

# Publication type.
# Legend: 0 = Uncategorized, 1 = Conference paper, 2 = Journal article,
# 3 = Preprint / Working Paper, 4 = Report, 5 = Book, 6 = Book section,
# 7 = Thesis, 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Visualization and Computer Graphics"
publication_short: "IEEE TVCG"

abstract: "Diagnosing the cluster-based performance of large-scale deep neural network (DNN) models during training is essential for improving training efficiency and reducing resource consumption. However, it remains challenging due to the incomprehensibility of the parallelization strategy and the sheer volume of complex data generated in the training processes. Prior works visually analyze performance profiles and timeline traces to identify anomalies from the perspective of individual devices in the cluster, which is not amenable for studying the root cause of anomalies. In this paper, we present a visual analytics approach that empowers analysts to visually explore the parallel training process of a DNN model and interactively diagnose the root cause of a performance issue. A set of design requirements is gathered through discussions with domain experts. We propose an enhanced execution flow of model operators for illustrating parallelization strategies within the computational graph layout. We design and implement an enhanced Marey's graph representation, which introduces the concept of time-span and a banded visual metaphor to convey training dynamics and help experts identify inefficient training processes. We also propose a visual aggregation technique to improve visualization efficiency. We evaluate our approach using case studies, a user study and expert interviews on two large-scale models run in a cluster, namely, the PanGu-α 13B model (40 layers), and the Resnet model (50 layers)."

# Summary. An optional shortened abstract.
summary: ""

tags:
  [
     "deep neural network", 
     "model training", 
     "parallel performance"
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
url_code:
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