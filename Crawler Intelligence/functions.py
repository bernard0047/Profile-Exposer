import keras
import os
import spacy
from pathlib import Path
import time
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
import warnings
import pandas as pd
import pickle


SEQUENCE_LENGTH = 300
tokenizer=Tokenizer()
OUTPUT_DIR='/Model_Names'


model=keras.models.load_model('crawler_intelligence.h5')
with open('tokenizer.pkl','rb') as f:
    tokenizer=pickle.load(f)
    
print("Loading from", OUTPUT_DIR)
nlp = spacy.load(OUTPUT_DIR)
   
def decode_sentiment(score):
    return 0 if score < 0.625 else 1
def predict(text):
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
    score = model.predict([x_test])[0]
    return decode_sentiment(score)
def get_names(t):
    doc = nlp(t)
    name=[]
    rest=[]
    #print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    for ent in doc.ents:
        if ent.label_=='PERSON':
            name.append(ent.text)

            return name
    return 0

