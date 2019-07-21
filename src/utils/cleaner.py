
def remove_emojies(string):
    import re
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


def clean_string(input):

    import string, re

    clean = str(input)
    table = str.maketrans({key: None for key in string.punctuation})
    clean = re.sub(r'(.)\1{3,}', r'\1',clean)
    clean = clean.translate(table)
    clean = clean.replace('nan','')
    clean = clean.strip()
    clean = clean.lower()

    clean = remove_emojies(clean)

    return clean


def correct_mispelling(input):

    from spellchecker import SpellChecker

    print(input)

    spell = SpellChecker()

    misspelled = spell.unknown(input.split(' '))

    corrected = input

    for word in misspelled:

        corrected = corrected.replace(word,spell.correction(word))

    print(corrected)

    return corrected
