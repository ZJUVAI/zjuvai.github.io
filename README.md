## 论文搬运说明

每篇论文对应/content/publication/下面的每一个文件夹；

文件夹里面要包括三个文件：

```
- index.md # 论文的信息，信息内容按照下面填写；
- featured.png/jpg # 论文的teaser或者其他
- feature.bib # 论文的bibtex引用
```

```
title: "Structuring Mobility Transition With an Adaptive Graph Representation." # 论文名称
authors:
  [
    Tianlong Gu,
    Minfeng Zhu,
    Wei Chen,
    Zhaosong Huang,
    Ross Maciejewski,
    and Liang Chang.,
  ] # 论文作者，按顺序填写
date: 2018-08-02T15:46:02+08:00 # 论文的发表日期，只要精确到月即可
doi: "" # 论文的doi
```

```
# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"] # 论文类型，从上面挑选即可
```

```
# 下面分别是论文发表的地方以及其缩写
# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Computational Social Systems"
publication_short: "IEEE TCSS"
```

```
# 论文abstract 不再多说，复制pdf的abstract时，注意换行
abstract: "Modeling human mobility is a critical task in fields such as urban planning, ecology, and epidemiology. Given the current use of mobile phones, there is an abundance of data that can be used to create models of high reliability. Existing techniques can reveal the macro-patterns of crowd movement or analyze the trajectory of a person; however, they typically focus on geographical characteristics. This paper presents a graph-based approach for structuring crowd mobility transition over multiple granularities in the context of social behavior. The key to our approach is an adaptive data representation, the adaptive mobility transition graph, that is globally generated from citywide human mobility data by defining the temporal trends of human mobility and the interleaved transitions between different mobility patterns. We describe the design, creation and manipulation of the adaptive mobility transition graph and introduce a visual analysis system that supports the multi-faceted exploration of citywide human mobility patterns."
```

```
# summary 有的话写上去，不知道写啥就不写了
# Summary. An optional shortened abstract.
summary: ""
```

```
# tags里面放上论文的key words
tags: ["Timeline, Mobility, Mobility Transition, Mobility Patterns"]
# category也不知道填点啥，能填就填，不能填就算了
categories: []
# featured 默认是false
featured: false
```

```
# 下面是论文的资源，填写方式都跟pdf一致，如果链接有多个，就跟 video那种写法即可
# pdf表示论文的pdf链接，直接用小组老博客上的那个链接即可
# code表示github地址
# dataset、poster、slides 如果有的话，最好能去找找
# source、project也就不要填了 已经去掉了
# video 如果老博客上有，就把链接拿过来；如果没有 去google vimeo上搜一下，可能会有的；

url_pdf:
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/AMTG.pdf
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/AMTG.mp4
  - http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/AMTG.mp4
```

```
# 以下这些内容不用改~
# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "featured"
  focal_point: "Top"
  preview_only: true

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
```

## 安装说明

1. 需要安装 hugo 和 hugo extended；
2. 先要 clone 这个项目，clone 之后，复制一个多的文件夹；
3. `git checkout -b content origin/content`
4. 再次 clone 这个项目（在第二部进行复制也可以），然后将 clone 下来的文件夹重命名为 docs
5. 然后按照 generate.bat 批处理文件中所示即可；
