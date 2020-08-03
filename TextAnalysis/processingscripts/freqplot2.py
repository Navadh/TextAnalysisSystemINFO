import nltk
import ssl
#nltk.data.path.append("/Users/rajeshpahari/PycharmProjects/untitled/venv/lib/python3.7/site-packages/nltk")
import sys
import codecs
from datascience import *
import numpy as np

#import matplotlib
# matplotlib.use('Agg', warn=False)
# %matplotlib inline
# import matplotlib.pyplot as plots
# plots.style.use('fivethirtyeight')

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

def freqtable(input_file):

    all_stopwords = set(nltk.corpus.stopwords.words('english'))
    #input_file = fileprovided
    fp = codecs.open(input_file, 'r', 'utf-8')
    words = nltk.word_tokenize(fp.read())

    # Remove single-character tokens (mostly punctuation)
    words = [word for word in words if len(word) > 1]

    # Remove numbers
    words = [word for word in words if not word.isnumeric()]

    # Remove alphanumeric
    words = [word for word in words if word.isalpha()]

    # Lowercase all words (default_stopwords are lowercase too)
    words = [word.lower() for word in words]

    # Remove stopwords
    words = [word for word in words if word not in all_stopwords]

    # Calculate frequency distribution
    fdist = nltk.FreqDist(words)
    wordarray = make_array()
    frequencyarray = make_array()
    for i in np.arange(10):
        wordthistime = fdist.most_common(10)[i][0]
        fequencythistime = fdist.most_common(10)[i][1]
        wordarray = np.append(wordarray, wordthistime)
        frequencyarray = np.append(frequencyarray, fequencythistime)

    table1 = Table().with_columns("Word", wordarray, "frequency", frequencyarray)

    #return table1
    return str(table1[0][0])
