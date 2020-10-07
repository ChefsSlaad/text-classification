#!/usr/bin/python3

import unicodedata
import spacy
import pandas as pd
from itertools import groupby
from collections import Counter
from datetime import datetime
import re


types_converter = {'EVENT_DATE': 'DATE',
                   'CHANNEL_TYPE': 'STRING',
                   'DESCRIPTION': 'STRING',
                   'RELATIONNUMBER': 'INT',
                   'Particulier_rol': 'INT',
                   'Zakelijk_rol': 'INT',
                   'TYPE_KLANT': 'STRING',
                   'GENDER': 'STR',
                   'AGE_CLASS_DESCRIPTION': 'STRING',
                   'PRODCOMBI_NEW': 'STRING',
                   'OPTIN': 'STRING',
                   'LABEL': 'STRING',
                   'HOOFDLABEL': 'STRING',
                   'APP_user': 'INT',
                   'IB_user': 'INT'
                }
class normalizer:

    def __init__(self, word_set = 'nl_core_news_md'):
#        self.tokenize = spacy.load('nl_core_news_md')
        pass

    def bag_of_words(self, dataset, column='DESCRIPTION'):
        if column == None:
            textblock = dataset
        else:
            textblock = dataset[column]
        return Counter(self.pre_process_text(textblock))

    def remove_accent_characters(self, textblock):
        """
        remove and replace all non-asci unicode characters. return the
        textblock with the asci equivalent
        """

        nfkd_form = unicodedata.normalize('NFKD', textblock)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


    def is_stop_word(input_string, lang='dutch'):
        """
        return true if a word is a stop word.
        language defaults to dutch
        other languages not implemented yet
        """

        return input_string in spacy.lang.nl.stop_words.STOP_WORDS

    def spellcheck(self, word):

        """
        spellcheck checks the spelling of the word and retuns a corrected
        word in the case of a spelling error
        """
        return word # not implemented

    def pre_process_text(self, textblock):
        result = []
        for word in self.tokenize(self.remove_accent_characters(textblock)):
            word = self.spellcheck(word)
            lem = word.lemma_
            if not (self.is_stop_word(lem) or word.is_punct or word.is_space) :
                result.append(lem)
        return result

    def read_csv_file(self, filename):
        """
        parses a csv file and returns it as a dict record
        """
        with open(filename, 'r') as f:
            # look for lines that follow the pattern
            # newline "YYYY-MM-DD
            # and split along that pattern
            # some other housekeeping:
            #    * remove the pattern ";;\n"
            #    * remove all the " symbols
            # also strip out the header row and return the full record

            fullfile = f.read()
            records = re.split(r'(^"\d{4}-\d{2}-\d{2})', fullfile,
                               flags=re.DOTALL | re.MULTILINE)

            header = records.pop(0)
            header = header.replace('"', '')
            header = header.replace(';;\n', '')
            header = header.split(',')
            records = [i+j for i, j in zip(records[0:len(records):2],
                                           records[1:len(records):2],)]
            data_file = []
            for rec in records:
                rec = rec.replace('"', '')
                rec = rec.replace(';;\n', '')
                rec = rec.replace(';\n', '')
                splitrec = rec.split(',', 2)
                tempsplitrec = splitrec.pop(2)[::-1].split(',', 12)
                for i in range(len(tempsplitrec)):
                    splitrec.append(tempsplitrec.pop()[::-1])
                rec = dict(zip(header, splitrec))
                data_file.append(rec)

        return data_file

    def convert_data_types(self, data_file, types_converter):
        for line in data_file:
            for k, v in line.items():
                print(k,v)
                datatype = types_converter.setdefault(k, 'STRING')
                if datatype == 'STRING':
                    line[k] = v
                elif datatype == 'INT':
                    if len(v) > 0:
                        line[k] = int(v)
                elif datatype == 'DATE':
                    if len(v) == 10:
                        line[k] = datetime.strptime(v, "%Y-%m-%d")
        return data_file

if __name__ == '__main__':
    my_normalizer = normalizer()
    datafile = my_normalizer.read_csv_file('sample_Marc.csv')
    datafile = my_normalizer.convert_data_types(datafile, types_converter)
    #print(datafile[0])

    df = pd.DataFrame(datafile)
    print(df)
#    BoW = my_normalizer.bag_of_words(record,)

#    for record in datafile:
#        record.append(my_normalizer.bag_of_words(record, column_id=2))
#    print(record)
#    print(BoW)


#    for record in datafile:
#        print(record)
#        BoW = my_normalizer.bag_of_words(record, column_id=2)
#        print(BoW)
