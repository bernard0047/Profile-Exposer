import keras
import os
import spacy
from pathlib import Path
import time
import warnings
import pandas as pd

OUTPUT1='NER Models/Name/content/Model'
OUTPUT2='NER Models/Prefix/content/Model'
OUTPUT3='NER Models/Position Held/Model'
OUTPUT4='NER Models/Intelligence/Model'

    
nlp_Name = spacy.load(OUTPUT1)
nlp_Pref = spacy.load(OUTPUT2)
nlp_Min = spacy.load(OUTPUT3)
nlpIntel=spacy.load(OUTPUT4)


def pred(tag):
    tag = tag.strip()
    if(tag.isnumeric()):
        return 1
    doc = nlpIntel(tag)
    #print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    for ent in doc.ents:
        if ent.text!=0:
            print(tag)
            return 1
    return 0


