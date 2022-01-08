# PaddleOCR PyWebIO Demo

> 使用PyWebIO部署PaddleOCR应用

体验地址：<http://39.106.32.208:8888>

## 介绍

1. PaddleOCR

   官网

   - <https://github.com/PaddlePaddle/PaddleOCR>

   官方介绍

   > PaddleOCR旨在打造一套丰富、领先、且实用的OCR工具库，助力开发者训练出更好的模型，并应用落地。

2. PyWebIO

   官网

   - <https://pywebio.readthedocs.io>
   - <https://github.com/pywebio/PyWebIO>

   官方介绍

   > Write interactive web app in script way.

## 开发步骤

注意：请使用Linux系统进行开发（原因：paddleocr的whl包对Windows的支持不太好）

### 1 创建Python环境

```sh
$ conda create --name pywebio python=3.9

# 进入环境
$ conda activate pywebio
```

### 2 安装相关依赖

```sh
$ pip install pywebio

# 以下为安装 paddleocr whl包需要
$ sudo apt install gcc build-essential

$ pip install "paddleocr>=2.0.1"
$ pip install paddlepaddle==2.2.1 -i https://mirror.baidu.com/pypi/simple
```

### 3 运行

```sh
$ python app.py
```
