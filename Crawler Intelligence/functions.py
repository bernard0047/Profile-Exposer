import keras
import os
import time
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import warnings
import pandas as pd


SEQUENCE_LENGTH = 300
tokenizer = Tokenizer()
warnings.filterwarnings('ignore')

df=pd.read_csv('strike.csv',sep='|')

tokenizer = Tokenizer()
tokenizer.fit_on_texts(df.text)

vocab_size = len(tokenizer.word_index) + 1
print("Total words", vocab_size)


def decode_sentiment(score):
    
    return 0 if score < 0.625 else 1


model=keras.models.load_model('crawl_intelligence.h5')

print(decode_sentiment("Ordnance Survey	"))

def tester():
    y_pred_1d = []
    y_test_1d = list(y_train)
    scores = model.predict(x_train, verbose=1, batch_size=8000)
    y_pred_1d = [decode_sentiment(score) for score in scores]

def plot_confusion_matrix(cm, classes,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """

    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, fontsize=30)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=90, fontsize=22)
    plt.yticks(tick_marks, classes, fontsize=22)

    fmt = '.2f'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label', fontsize=25)
    plt.xlabel('Predicted label', fontsize=25)


cnf_matrix = confusion_matrix(y_test_1d, y_pred_1d)
plt.figure(figsize=(12,12))
plot_confusion_matrix(cnf_matrix, classes=df.scrape.unique(), title="Confusion matrix")
plt.show()