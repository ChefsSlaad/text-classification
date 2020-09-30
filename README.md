# text-classification


stappen om tot een classificatie te komen:

1) Normaliseren van de text
    a) woorden splitsen (tokenize)
    b) accenten en leestekens verwijderen
    c) lower-case maken
    d) stop-woorden verwijderen
    e) stammen / lemmatiseren
    f) lemma's toevoegen (domeinspecifiek)

2) Tellen van de woorden in de text (bag of words)

3) Multi-regressie op labels
    a) data set splitsen in trainingsset en verificatie set
    b) LDA model toepassen op trainingsset
    c) verificatie met verificatieset





bronnen:
http://blog.refine-it.nl/begrijpend-lezen-met-python-en-nlp/
https://spacy.io/models/nl
https://stackabuse.com/python-for-nlp-tokenization-stemming-and-lemmatization-with-spacy-library/

https://towardsdatascience.com/text-classification-in-python-dd95d264c802
