import argparse
from wordcloud import WordCloud, STOPWORDS
from src.utils import utils
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def generate_word_cloud(df, mask_path=None, output=None, font=None):

    text = ' '.join('' if comment is None else str(comment) for comment in df)

    stopwords = set(STOPWORDS)
    stopwords.update(utils.get_stopwords())

    if mask_path is not None:
        plot_word_cloud_mask(text, stopwords, mask_path, font)

    else:
        plot_word_cloud(text, stopwords, font)

    plt.axis('off')

    if output is not None:
        plt.savefig(output, format="png")

    plt.show()


def plot_word_cloud_mask(text, stopwords, mask_path, font):

    mask, colors = get_mask(mask_path)
    wordcloud = WordCloud(font_path=font, width=1024, height=1024, stopwords=stopwords, random_state=42,
                          background_color='white', contour_width=15, min_font_size=15,
                          max_font_size=300, mask=mask).generate(text)

    plt.figure(figsize=[10, 10], dpi=200)

    plt.imshow(wordcloud.recolor(color_func=colors), interpolation="bilinear")


def plot_word_cloud(text, stopwords, font):

    wordcloud = WordCloud(font_path=font, width=1024, height=1024, stopwords=stopwords,
                          max_font_size=300, background_color='white').generate(text)

    plt.figure(figsize=[10, 10], dpi=200)

    plt.imshow(wordcloud, interpolation='bilinear')


def plot_bar_group(df, column, x, y):

    group = df.groupby(column)
    (group.size()/df.shape[0]).sort_values(ascending=False).head(10).plot.bar()

    plt.xticks(rotation=50)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()


def get_mask(mask_path):

    from PIL import Image
    from wordcloud import ImageColorGenerator
    import numpy as np

    mask = np.array(Image.open(mask_path))
    image_colors = ImageColorGenerator(mask)

    return mask, image_colors


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(description='Create Word Cloud from json')
    arg_parser.add_argument('--name', type=str, help='name of video page stored in data folder.', required=True)

    args = arg_parser.parse_args()

    from src.analysis import process

    df = process.get_processed_comments('../../data/{}_comments.csv'.format(args.name))

    generate_word_cloud(df['comment'], output='../../output/{}_cloud.png'.format(args.name))
