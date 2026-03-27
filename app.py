from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    file = request.files["image"]

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(OUTPUT_FOLDER, "output.png")

    file.save(input_path)

    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path)

    return render_template("index.html", output_image="/" + output_path)

if __name__ == "__main__":
    app.run(debug=True)