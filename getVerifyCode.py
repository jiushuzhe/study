from flask import Flask, request
from flask_cors import CORS
import ddddocr


app = Flask(__name__)
CORS(app, resources=r"/*")


@app.route('/get_code', methods=["POST"])
def get_code():
    img_bytes = request.json["img"]
    ocr = ddddocr.DdddOcr()
    # with open("/Users/edy/Desktop/yanzhengma.png", 'rb') as f:
    #     img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return res


if __name__ == '__main__':
    app.run(port=5001, debug=True)
