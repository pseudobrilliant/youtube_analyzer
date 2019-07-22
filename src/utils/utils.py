
def get_stopwords(path='../../data/stopwords.csv'):

    import os
    import pandas as pd

    stopwords = []

    if os.path.exists(path):
        with open(path, 'r') as flh:
            fields = ['stopword']
            df = pd.read_csv(flh, names=fields)

            stopwords = df['stopword'].values

    return stopwords


