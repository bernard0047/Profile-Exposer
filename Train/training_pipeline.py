# -*- coding: utf-8 -*-
import spacy
import re
import random
from spacy.util import minibatch, compounding
import os
from pathlib import Path
nlp=spacy.load('en_core_web_sm')

# Getting the pipeline component
ner=nlp.get_pipe("ner")


'''
This is a unified spacy custom train model pipeline and can be used regardless of the model structure
All training data has been curated by us using  https://manivannanmurugavel.github.io/annotating-tool/spacy-ner-annotator/
Get the train data for each model from the .txt files
'''

TRAIN_DATA=[('rotorua-lakes-council\r', {'entities': [(14, 21, 'text')]}), {'entities': [(47, 55, 'text'), (56, 62, 'text')]})] # this list has been truncated for demonstration

def trim_entity_spans(data: list) -> list:
    '''
    Removes leading and trailing white spaces from entity spans.

    Args:
        data (list): The data to be cleaned in spaCy JSON format.

    Returns:
        list: The cleaned data.
    '''
    invalid_span_tokens = re.compile(r'\s')

    cleaned_data = []
    for text, annotations in data:
        entities = annotations['entities']
        valid_entities = []
        for start, end, label in entities:
            valid_start = start
            valid_end = end
            while valid_start < len(text) and invalid_span_tokens.match(
                    text[valid_start]):
                valid_start += 1
            while valid_end > 1 and invalid_span_tokens.match(
                    text[valid_end - 1]):
                valid_end -= 1
            valid_entities.append([valid_start, valid_end, label])
        cleaned_data.append([text, {'entities': valid_entities}])

    return cleaned_data
#The above function checks that there are no empty spaces in the labels. For example Ministry and Ministry* where * is a space symbol should be considered as a single entity. Since we have curated the train data ourselves, such discrepancies might have crept in


TRAIN_DATA=trim_entity_spans(TRAIN_DATA)

#Add Entities to labels
for _, annotations in TRAIN_DATA:
  for ent in annotations.get("entities"):
    ner.add_label(ent[2])

pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]


#We run the below train loop for 50 iterations. Spacy learns really fast as compared to other NLP Models and works great on small input data too
# TRAINING THE MODEL
with nlp.disable_pipes(*unaffected_pipes):

  # Training for 50 iterations
  for iteration in range(50):

    # shuufling examples  before every iteration
    random.shuffle(TRAIN_DATA)
    losses = {}
    # batch up the examples using spaCy's minibatch
    batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        texts, annotations = zip(*batch)
        nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                    drop=0.35,  # dropout - make it harder to memorise data
                    losses=losses,
                )
        print("Losses", losses)


#Save the model to root folder
output_dir = Path('/content/Model')
nlp.to_disk(output_dir)
print("Saved model to", output_dir)

#Zip the model for easier accessibility and so that it can be easily integrated on local.
!zip -r /content/Model_Names.zip /content/Model