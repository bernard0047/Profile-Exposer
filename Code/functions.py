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
from Tkinter import *
from time import strftime

root = Tk()

time_var = StringVar()

def set_time():
    time_var.set(strftime('%H:%M:%S'))
    root.after(1000, set_time)

Label(root, bd=11, textvariable=time_var).pack()
set_time()
root.mainloop()

    
nlp_Name = spacy.load(OUTPUT1)
nlp_Pref = spacy.load(OUTPUT2)
nlp_Min = spacy.load(OUTPUT3)
nlpIntel = spacy.load(OUTPUT4)


def pred(tag):
    tag = tag.strip().lower()
    stop_words = ["external website"]
    for sw in stop_words:
        if sw in tag:
            return 0
    if(tag.isnumeric()):
        return 1
    doc = nlpIntel(tag)
    #print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    for ent in doc.ents:
        if ent.text!=0:
            #print(tag)
            return 1
    return 0
