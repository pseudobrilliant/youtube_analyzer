import pandas as pd
from src.utils import cleaner
from src.analysis import language_detect


def get_processed_comments(path):

    with open(path, 'r') as f:

        df = pd.read_csv(f)

        df = clean_comments(df)

        df = get_comment_language(df)

        return df


def clean_comments(df):

    df['comment'] = df['comment'].apply(lambda x: cleaner.clean_string(x))

    return df


def get_comment_language(df):

    languages = []

    for comment in df['comment']:
        lang = language_detect.detect(comment)
        languages.append(lang)

    df = df.assign(lang=languages)

    return df
