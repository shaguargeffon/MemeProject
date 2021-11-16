"""A python module to generate a random meme using CLI."""

import os
import random
import argparse
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeGenerator.MemeGenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/Naruto/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/NarutoQuotes/NarutoQuotesTXT.txt',
                       './_data/NarutoQuotes/NarutoQuotesDOCX.docx',
                       './_data/NarutoQuotes/NarutoQuotesPDF.pdf',
                       './_data/NarutoQuotes/NarutoQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


def write_share_meme_email(meme_path):
    """Write meme path to txt file."""
    with open('share.txt', 'w') as f:
        f.write(meme_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a meme.")
    parser.add_argument('--path', type=str, default=None, help="Path to image")
    parser.add_argument('--body', type=str,
                        default=None,
                        help="body to be added to image")
    parser.add_argument('--author', type=str,
                        default=None,
                        help="author to be added to image")
    args = parser.parse_args()
    meme_output = generate_meme(args.path, args.body, args.author)
    print(meme_output)
    write_share_meme_email(meme_output)
