import os
from flask import Flask, render_template, request, send_from_directory

## UNCOMMENT THIS CODE WHEN RUNNING ON GOOGLE COLAB ##
# from big_sleep import Imagine
# import shutil

# def run_dreams(txt, Learning_rate, Number_of_iterations, Number_of_epochs, Seed):
#     dream = Imagine(
#         text = txt,
#         save_every = 5,
#         save_progress = True,
#         lr = Learning_rate,
#         iterations = Number_of_iterations,
#         epochs = Number_of_epochs,
#         seed = Seed
#     )
#     return dream()

# def get_file(txt):
#     spl = txt.split()
#     GA_file = '_'.join(spl)
#     return f"{GA_file}.png"

# def save_files(txt):
#     GA_file = get_file(txt)
#     return shutil.move(f'/content/{GA_file}', f'/content/gdrive/MyDrive/GenerativeArt/static/Images/{GA_file}')

app = Flask(__name__)

IMAGE_FOLDER = "static/Images"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

text_records = {}

# Home Page
@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")

# Generate Art Page
@app.route("/generate-art/")
def generate_art():
    return render_template("generate-art.html")

@app.route('/text', methods = ['POST','GET'])
def display_text():
    output = request.form.to_dict()
    text = output["text"]
    text_records['text'] = text
    return render_template("generate-art.html", text = text)

## UNCOMMENT THIS CODE WHEN RUNNING ON GOOGLE COLAB ##
# @app.route('/run', methods = ['POST','GET'])
# def execute_dreams():
#   if text_records['text']:
#       run_dreams(text_records['text'], 0.10, 10, 1, 300)
#       save_files(text_records['text'])
#       g_a = get_file(text_records['text'])
#       return render_template("generate-art.html", generated_image = IMAGE_FOLDER + f"/{g_a}", response = "Successfully Generated")
#   else:
#       return render_template("generate-art.html", response = "No Text was given")



# Mint NFTs Page
@app.route("/mint-nft/")
def nft():
    return render_template("nft.html")

# Images Page
@app.route("/images/")
def images():
    return render_template("images.html")

@app.route('/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['IMAGE_FOLDER'],
                               filename)


if __name__ == "__main__":
    app.run(debug=True)