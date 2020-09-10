#!/usr/bin/python3

import nltk
import unicodedata
import string


def tokenize(textblock):
    return nltk.word_tokenize(textblock)


def remove_accent_characters(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def convert_to_lowercase(input_string):
    return word.lower()


def remove_punctuation_characters(input_string):
    return u"".join([l for l in input_string if l not in string.punctuation])


def is_stop_word(input_string, lang='dutch'):
    return input_string in set(nltk.corpus.stopwords.words('dutch'))

def pre_process_text(textblock):
    result = []
    for word in tokenize(textblock):
        word = remove_punctuation_characters(
               remove_accent_characters(
               word.lower(
               )))
        if word != '' and not is_stop_word(word):
            result.append(word)
    return result


in_5 = r"""
                We gaan naar het zwembad én naar de speeltuin!
                Koop nú nieuwe loten.
                Frans Langer, dé behanger.
                We hebben daar zó lang staan wachten.
                Niet lanterfanten, wérken!
                Inleveren vóór 1 december.
                Was het maar wáár!
                Schrééuw niet zo!
                Dóé iets!
                Déúr dicht!
                Níéts zeggen
                """

if __name__ == '__main__':
    print(pre_process_text(in_5))
