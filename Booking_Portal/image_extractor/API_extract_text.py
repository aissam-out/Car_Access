from flask import Flask, jsonify
from utils import crop, togrey, extact_text

app = Flask(__name__)

image_path = "images/cin5.jpg"
cropped_image = 'cropped.jpg'
grey_image = "greyscale.png"

@app.route("/")
def extract_api():
    c_img = crop(image_path, cropped_image)
    g_img = togrey(cropped_image, grey_image)
    text = extact_text(grey_image)
    resp = jsonify(dataID=text)
    resp.headers['Access-Control-Allow-Origin']='*'

    return resp

if __name__ == "__main__":
    app.run()
