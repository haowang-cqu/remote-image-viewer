import os
from PIL import Image
import mimetypes
from typing import List, Any
from flask import Flask, render_template, abort, send_file, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/image/<path:image_path>")
def get_image(image_path: str):
    image_path = os.path.join("/", image_path)
    if not os.path.isfile(image_path):
        abort(404, description="file not exist")
    mimetype = mimetypes.guess_type(image_path, strict=True)[0]
    return send_file(image_path, mimetype=mimetype)


@app.route("/info/<path:image_path>")
def get_image_info(image_path: str):
    image_path = os.path.join("/", image_path)
    if not os.path.isfile(image_path):
        return jsonify({"code": 1, "msg": "file not exist"})
    img = Image.open(image_path)
    return jsonify({
        "path": image_path,
        "width": img.width,
        "height": img.height
    })


def pagination(data: List[Any], page_num: int, page_size: int):
    """分页器
    """
    if len(data) == 0:
        return {
            "total": 0,
            "pages": 0,
            "pageNum": 0,
            "pageSize": page_size,
            "list": [],
        }
    # 计算总分页数
    total = len(data)
    pages = total // page_size
    if total % page_size != 0:
        pages += 1
    # 修正错误的页码
    if page_num > pages:
        page_num = pages
    if page_num < 1:
        page_num = 1
    # 计算开始和结束位置
    start = (page_num - 1) * page_size
    end = start + page_size
    return {
        "total": total,
        "pages": pages,
        "pageNum": page_num,
        "pageSize": page_size,
        "list": data[start:end],
        "size": len(data[start:end]),
    }


@app.route("/list")
def list_images():
    path = request.args.get("path", None, type=str)
    page_num = request.args.get("pageNum", 1, type=int)
    page_size = request.args.get("pageSize", 20, type=int)
    if path == None or page_num < 1 or page_size < 0:
        return jsonify({"code": 1, "msg": "invalid query parameters"})
    if not os.path.isdir(path):
        return jsonify({"code": 2, "msg": "invalid path"})
    images = os.listdir(path)
    images.sort()
    images = list(map(lambda image: os.path.join(path, image), images))
    page = pagination(images, page_num, page_size)
    return jsonify({"code": 0, "msg": "success", "page": page})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=6789
    )
