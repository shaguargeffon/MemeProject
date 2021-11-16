"""A python module to generate random meme on web."""


import random
import os
import requests
from MemeGenerator.MemeGenerator import MemeEngine
from QuoteEngine.Ingestor import Ingestor
from flask import Flask, render_template, request

app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/NarutoQuotes/NarutoQuotesTXT.txt',
                   './_data/NarutoQuotes/NarutoQuotesDOCX.docx',
                   './_data/NarutoQuotes/NarutoQuotesPDF.pdf',
                   './_data/NarutoQuotes/NarutoQuotesCSV.csv']

    quotes_total = list()
    for qf in quote_files:
        absolute_path = os.path.abspath('.') + qf[1:]
        quote_list = Ingestor.parse(absolute_path)
        quotes_total.extend(quote_list)

    # quote_files variable

    images_path = os.path.abspath('.') + "/_data/photos/Naruto/"

    images = [images_path + x for x in os.listdir(images_path)]

    return quotes_total, images


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    if not imgs:
        raise Exception("Under the given image path there is no image.")

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    url_extension = url.split('.')[-1]

    if url_extension.lower() not in ['jpg', 'jpeg', 'png']:
        raise Exception("The input image format can not be handled.")

    image_content = requests.get(url, stream=True).content
    temp_image_name = './temp.' + 'jpg'
    with open(temp_image_name, 'wb') as f:
        f.write(image_content)

    meme_path = meme.make_meme(temp_image_name, body, author)
    os.remove(temp_image_name)
    return render_template('meme.html', path=meme_path)


if __name__ == "__main__":
    app.run()
