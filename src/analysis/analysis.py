import argparse
import pandas as pd
from src.utils import cleaner
from src.analysis import language_detect
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np


def generate_word_cloud(df):

    text = ' '.join('' if comment is None else str(comment) for comment in df)

    stopwords = set(STOPWORDS)
    stopwords.update(['sinner', 'saw', 'say', 'even', 'watch', 'sooo','im','oh'])

    wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color='black').generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def plot_bar_group(df, column, x, y):

    group = df.groupby(column)
    (group.size()/df.shape[0]).sort_values(ascending=False).head(10).plot.bar()

    plt.xticks(rotation=50)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()


def process_dataframe(df):

    df['comment'] = df['comment'].apply(lambda x: cleaner.clean_string(x))

    languages = []

    for comment in df['comment']:
        languages.append(language_detect.detect(comment))

    df = df.assign(lang=languages)

    return df


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(description='Create Word Cloud from json')
    arg_parser.add_argument('--name', type=str, help='name of video page stored in data folder.', required=True)

    args = arg_parser.parse_args()

    with open('../../data/{}_comments.csv'.format(args.name), 'r') as f:

        df = pd.read_csv(f)

        df = process_dataframe(df)

        generate_word_cloud(df['comment'])

        generate_word_cloud(df.loc[df['lang'] == 'Spanish']['comment'])

        generate_word_cloud(df.loc[df['lang'] == 'Russian']['comment'])

        plot_bar_group(df, 'lang', 'country', 'count')
