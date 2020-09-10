#!/usr/bin/python3

import unicodedata
import string
import nltk

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


in_3 = r"""
    Al maanden problemen met het WiFi netwerk in huis. Volgens mijn abonnement
    moet ik een downloadsnelheid hebben van 250 mbps. Echter de verschillende
    speeltoestel laten zien dat de downloadsnelheid niet meer is dan 45 mbps.
    Gevolg Met thuiswerken knalt de verbinding er constant uit bij
    Microsoftteams.
    Omdat mijn dochter volgend week examen moet doen is de betrouwbaarheid
    van de verbinding belangrijk. Na veel gedoe zou er nu eindelijk een
    monteur langs komen. Volgens De website van Ziggo stuurt de monteur een
    SMS als hij onderweg is. Geen sms gehad wel een gesprek gemist omdat
    ik in een conference call zat. Blijkt de monteur bij de buren te hebben
    gestaan en daar een briefje in de bus gegooid. Ook niet aangebeld
    want mijn buurman was thuis.
    Ziggo vervolgens gebeld. Antwoord: de monteur heeft u 4 keer gebeld
    waarvan 2 keer op de vaste aansluiting. Helaas heb ik geen vaste
    aansluiting dus puur onzin. Ik was gewoon thuis. Reactie Ziggo: we gaan de
    monteur opnieuw inplannen. Volgende week dus. Krijg ik de volgende dag een
    mail met een rekening van €85 voorrijkosten en kosten reparatie. Deze mail
    is een dag later kennelijk door Ziggo uit mijn mailbox verwijderd. Ik heb
    gelukkig een kopie gemaakt.
    Opnieuw contact met Ziggo waarbij de klantenservice geen uitleg kan geven.
    Deze dame had kennelijk het dossier niet gelezen met de eerdere contacten.
    Reactie begon direct met Ziggo garandeerd 20mbps. Op mijn vraag waarom mijn
    abonnement 250 mbps is en ik veel meer moet betalen kwam een ontwijkend
    antwoord.
    Ik kijk nu uit naar de aanleg van glasvezel door de KPN. Ik stap dan
    gelijk over. Wat een waardeloos bedrijf Ziggo.
    """

in_4 = r"""
    Wat een vreselijke zaak . Na alles gelezen te hebben zijn wij
    niet de enige met klachten . Twee weken geleden wasmachine besteld
    en betaald . Al drie keer moeten bellen en ze behandelen je als oud
    vuil . Zeer invriendelijk niks wetend personeel. Chefs en leidinggevende
    krijg je never nooit te spreken . Wel geld innen maar niks leveren
    en dan zeggen geduld hebben 😱
    Denk dat het tijd wordt dat wij consumentenbond en radar moeten gaan
    inschakelen want mediamarkt MOET gestopt worden !!! Duizenden
    gedupeerden inmiddels . Wat is dit ? Ik heb inmiddels op verschillende
    sites en media’s een klacht ingediend en het verhaal verteld van ons
    en duizenden anderen 😡. Net een pipo aan de lijn , een meisje wat
    totaal niet klantvriendelijk is enz .. en wat zegt deze domme tut;
    u kiest hier zelf voor
       """
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
    print(pre_process_text(in_4))
