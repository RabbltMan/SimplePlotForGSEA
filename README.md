# 极简的GSEA图表生成脚本
### 可执行文件(.exe)下载

[🔗下载链接](https://rabbltman.lanzout.com/i29Pm148q09e)

密码：54du

### 说明
- 您可以在程序界面中**选择基因列表文件**，无需将脚本与基因列表放在同目录下。但请注意，**程序生成的图表将保存在.exe文件的同目录下**。
- 您需要确保您的基因列表文件的样式与 [```ExampleGenelist.txt```](https://github.com/RabbltMan/SimplePlotForGSEA/blob/master/ExampleGenelist.txt) 一致。这包括：
    - **.txt** 的文件格式
    - 每个基因**单独成行，且不要有空格或符号**
---
### 关于程序
- 适用于网络药理学等。若您没有任何计算机程序设计基础，使用这个带有UI界面的脚本可以完全摆脱代码，一键完成 **```GO富集```** 和 **```KEGG富集```** 的图表生成。
- 使用了 GSEApy 库 [[PyPI](https://pypi.org/project/gseapy/) | [Repo](https://github.com/zqfang/GSEApy) | [Docs](https://gseapy.readthedocs.io/en/latest/index.html)] 用于进行**富集分析**。
---
### 关于源代码和笔记本文件使用
[![Static Badge](https://img.shields.io/badge/python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=3776AB)](https://python.org/)
- 若您有一定的编程基础并有条件在您的设备上运行 python 程序，则可以：
  - 打开或编辑带有UI界面的 ```EnrichmentPlotGenerator.py``` 文件（这是一个标准Python文件）

  
  - 或运行 ```EnrichmentPlotNotebook.ipynb```（这是一个Jupyter Notebook编写的Python文件，可以分步执行每步操作，且代码更简单）

- 若您使用 **Anaconda** ，脚本所需的第三方库和虚拟环境创建方法已附于```requirements.txt```。如果您有需求但不会用，可以尝试在 **[Issues](https://github.com/RabbltMan/SimplePlotForGSEA/issues)** 中提出，RabbltMan **不一定能提供帮助**。

- 需要脚本修改可以参考[文档](https://gseapy.readthedocs.io/en/latest/index.html) 。若脚本有 bug 欢迎在 **[Issues](https://github.com/RabbltMan/SimplePlotForGSEA/issues)** 中提出，有好的想法欢迎 **[Pull Requests](https://github.com/RabbltMan/SimplePlotForGSEA/pulls)**。
---
### 其他
如有问题可以开个 **[Issue](https://github.com/RabbltMan/SimplePlotForGSEA/issues)**，也可直接邮件联系 rabbltman@outlook.com。

~~如果您愿意的话可以给我打钱。~~ RabbltMan 不主张打赏、捐赠或赞助。
