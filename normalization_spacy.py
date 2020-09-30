#!/usr/bin/python3

import unicodedata
import spacy
import numpy
from itertools import groupby
from collections import Counter
import re


class normalizer:

    def __init__(self, word_set = 'nl_core_news_md'):
#        self.tokenize = spacy.load('nl_core_news_md')
        pass

    def bag_of_words(self, textblock):
        return Counter(self.pre_process_text(textblock))

    def remove_accent_characters(self, textblock):
        """
            remove and replace all non-asci unicode characters. return the
            textblock with the asci equivalent
        """
        nfkd_form = unicodedata.normalize('NFKD', textblock)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

    def is_stop_word(input_string, lang='dutch'):
        return input_string in spacy.lang.nl.stop_words.STOP_WORDS

    def spellcheck(self, word):
        """
        spellcheck checks the spelling of the word and retuns a corrected
        word in the case of a spelling error
        """
        return word # not implemented

    def pre_process_text(self, textblock):
        result = []
        for word in tokenize(remove_accent_characters(textblock)):
            word = spellcheck(word)
            lem = word.lemma_
            if not (is_stop_word(lem) or word.is_punct or word.is_space) :
                result.append(lem)
        return result

    def read_csv_file(self, filename):
        """
        parses a csv file and returns a dataframe containing the record
        as well as the following metadata:
        * bag of words
        """
        with open(filename, 'r') as f:

            # look for lines that follow the pattern
            # newline "YYYY-MM-DD
            # and split along that pattern
            fullfile = f.read()
            records = re.split(r'(^"\d{4}-\d{2}-\d{2})', fullfile, flags=re.DOTALL|re.MULTILINE)
            records.pop(0)
            records = [i+j for i, j in zip(records[0:len(records):2],
                                           records[1:len(records):2],)]
            for r in records:
                print(r.split(','))

if __name__ == '__main__':
    my_normalizer = normalizer()
    my_normalizer.read_csv_file('sample_Marc.csv')
