# 浙江大学可视分析小组主页

<!-- [国际镜像](http://zjuvai.cn/) -->

# 小组主页页面的更新

小组主页目前由[温圳](https://github.com/KidsXH/)在进行维护；

小组主页在腾讯云上购买了域名，并绑定了域名解析（目前用了@朱闽峰 的账号）；

小组目前的主页地址是：[https://zjuvai.cn](https://zjuvai.cn/)；采用了 hugo+github 主页托管的形式，然后进行域名重定向（原网址：zjuvai.github.io）。

主页基于 Academic 的 hugo 主题，但是已经对其进行了大量的修改，所以有不太一致的地方。

## 如何在本地初始化？

现在，有两个分支：master 分支和 content 分支；因为 github 要求 github.io 的托管页面，只能托管在名为 user-name.github.io 这个 repo 的 master 分支上；所以现在，master 分支上托管了生成好的页面，content 分支上托管了内容。<br />

1. 你需要有一个 github 账户，并且需要成为 ZJUVAI 组织的成员；
2. clone 该项目：`git clone git@github.com:ZJUVAI/zjuvai.github.io.git`
3. 到此为止，你已经把资源文件都下载下来了；但是你可能还需要安装 hugo-extended；
   1. 在 github 的 release 页面，找到最新的 hugo_extended 版本：[https://github.com/gohugoio/hugo/releases/](https://github.com/gohugoio/hugo/releases/)，一般而言，它的名字都是 hugo_extended_version_OS-bits.zip
   2. 解压后，放在某个目录下，然后将该目录添加到你的环境变量中，启动行命令测试一下是否添加成功。

## 如何修改主页？

在这之前，我们先来熟悉一下整个文件目录。

```bash
├── config
├── content
│   ├── accomplishments
│   ├── authors
│   ├── home
|   ├── members
|   ├── publications
|   ├── talks
├── data
├── docs
├── resources
├── scripts
├── static
├── themes
├── .editorconfig
├── .gitignore
├── .gitmodules
├── generate.bat
├── LICENSE.md
├── README.md
├── update_academic.sh
└── view.sh
```

其中几乎所有内容都被存放在 content 目录下：

- accomplishments 存着 PaperCollection 这个页面的内容；
- authors 存着小组成员名单；
- home 则是主页的相关信息；
- members 主要提供 members 这个页面，内容都来自于 authors 这个文件夹；
- publications 下面是主页 Publications 下面的文章；
- talks 下面是主页 Talks 下面的内容；

还有一些比较重要的文件夹：

- docs：每次新生成的主页页面都会存进 docs 文件夹下面；它必须包含一个 CNAME 文件，指向现在的域名：zjuvai.cn；
- themes：存着我修改过的 academic 主题；

生成新的静态页面并部署：`npm run deploy`
