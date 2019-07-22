import string
from nltk.tokenize import word_tokenize
import re

def remove_emojies(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\u200d"
                               u"\u2640-\u2642"
                               "]+", flags=re.UNICODE)

    clean = emoji_pattern.sub(r'', string)

    return clean


# Found on https://towardsdatascience.com/how-to-implement-seq2seq-lstm-model-in-keras-shortcutnlp-6f355f3e5639
def sentence_cleanup(sentence):

    sentence = re.sub(r"’", "'", sentence)
    sentence = re.sub(r"i'm", "i am", sentence)
    sentence = re.sub(r"he's", "he is", sentence)
    sentence = re.sub(r"she's", "she is", sentence)
    sentence = re.sub(r"it's", "it is", sentence)
    sentence = re.sub(r"that's", "that is", sentence)
    sentence = re.sub(r"what's", "that is", sentence)
    sentence = re.sub(r"where's", "where is", sentence)
    sentence = re.sub(r"how's", "how is", sentence)
    sentence = re.sub(r"\'ll", " will", sentence)
    sentence = re.sub(r"\'ve", " have", sentence)
    sentence = re.sub(r"\'re", " are", sentence)
    sentence = re.sub(r"\'d", " would", sentence)
    sentence = re.sub(r"\'re", " are", sentence)
    sentence = re.sub(r"won't", "will not", sentence)
    sentence = re.sub(r"can't", "cannot", sentence)
    sentence = re.sub(r"n't", " not", sentence)
    sentence = re.sub(r"n'", "ng", sentence)
    sentence = re.sub(r"'bout", "about", sentence)
    sentence = re.sub(r"'til", "until", sentence)
    sentence = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", sentence)

    tokenized = word_tokenize(sentence)

    transform = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(transform) for w in tokenized]
    words = ' '.join(stripped)

    return words


def correct_mispelling(input):

    from spellchecker import SpellChecker

    print(input)

    spell = SpellChecker()

    misspelled = spell.unknown(spell.split_words(input))

    corrected = input

    for word in misspelled:

            candidates = spell.candidates(word)

            print(candidates)

            corrected = corrected.replace(' ' + word + ' ', ' ' + spell.correction(word) + ' ')

    print(corrected)

    return corrected


def clean_string(input):

    clean = str(input)
    clean = re.sub(r'( )\1{2,}', r'\1', clean)
    clean = re.sub(r'(.)\1{3,}', r'\1',clean)
    clean = sentence_cleanup(clean)
    clean = clean.replace('nan','')
    clean = clean.strip()
    clean = clean.lower()

    clean = remove_emojies(clean)

    return clean
