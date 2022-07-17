# 远程图片查看器
## 是什么？
顾名思义，远程图片查看器是一个通过浏览器查看远程服务器上图片的工具。远程开发是深度学习研究过程中的常用手段，在没有图形化界面的远程终端中查看图片就成了一个问题。通常我们可以用下面这几种手段查看远程服务器上的图片：

1. 通过各种文件传输方式下载到本地查看，如 FTP、SFTP、rz/sz
2. 使用远程开发软件查看，如 VS Code、Jupyter Notebook
3. ...

虽然这些方式查看少量图片比较方便，但是对于具有上万图片的数据集就显得有些乏力看。为了改善这种情况，该仓库中实现了一个基于浏览器的远程图片查看器，它具有如下优点：

1. 可以浏览图片文件夹或查看单张图片
2. 采用 B/S 架构
3. 前后端分离

## 运行
### 克隆仓库
```bash
git clone https://github.com/WangHaoCS/remote-image-viewer.git
cd remote-image-viewer
```
### （可选）创建虚拟环境
这里以 venv 为例，也可以使用 conda 或者 virtualenv
```bash
python -m venv .venv
source .venv/bin/activate # 激活虚拟环境
```
### 安装依赖
```bash
pip install -r requirements.txt
```
### 运行程序
```bash
python riv.py
```

## 使用
### 查看单张图片
浏览器访问 `http://IP地址:6789/image/图片绝对路径` 即可查看服务器上的某张图片，如下图所示
![查看单张图片](/images/single.png)

### 浏览图片文件夹
浏览器访问 `http://IP地址:6789`，输入图片文件夹路径即可浏览图片文件夹，如下图所示
![缩率图](/images/thumbnail.png)

点击任意缩略图即可查看大图，如下图所示
![查看大图](/images/fancybox.png)