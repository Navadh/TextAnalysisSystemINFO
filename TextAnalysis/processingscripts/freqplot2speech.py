import nltk
import ssl
#nltk.data.path.append("/Users/rajeshpahari/PycharmProjects/untitled/venv/lib/python3.7/site-packages/nltk")
import sys
import codecs
from datascience import *
import numpy as np
import pandas as pd
import os
import matplotlib
# matplotlib.use('Agg', warn=False)
matplotlib.use('agg')
#%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
from nltk.tag import pos_tag

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from TextAnalysisSystem3.settings import STATICIMAGE_DIR

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
    plots.figure(figsize=(20,10))
    table1.barh(0)
    plots.title("Top 10 word frequency count")
    locationtosavefile = STATICIMAGE_DIR + "/text1.png"
    #locationtosavefile = os.path.join(STATICFILES_DIRS, "/images/text1.png")
    plots.savefig(locationtosavefile,bbox_inches="tight")
    #plots.savefig('/Users/rajeshpahari/PycharmProjects/FinalProject/media/text1.png',bbox_inches="tight")
    #return table1

    completewordarray = make_array()
    completefrequencyarray = make_array()
    for i in np.arange(len(fdist)):
        wordthistime2 = fdist.most_common(len(fdist))[i][0]
        fequencythistime2 = fdist.most_common(len(fdist))[i][1]
        completewordarray = np.append(completewordarray, wordthistime2)
        completefrequencyarray = np.append(completefrequencyarray, fequencythistime2)

    table2 = Table().with_columns("Word", completewordarray, "frequency", completefrequencyarray)
    table3 = table2.sort("frequency")
    leastfrequentwords = table3.take(np.arange(30))[0].flatten()
    sentence = ''
    for i in np.arange(30):
        sentence = sentence + ' ' + leastfrequentwords[i] + ' '

    abc = nltk.pos_tag(nltk.word_tokenize(sentence))
    dfObj = pd.DataFrame(abc)
    dfconverted = dfObj.rename(columns={0: 'word'}).rename(columns={1: 'Part of Speech'})
    speechtable = Table.from_df(dfconverted)
    locationtosavefile = STATICIMAGE_DIR + "/partofspeechanalysis.csv"
    speechtable.to_csv(locationtosavefile)
    html = speechtable.as_html()
    locationofhtmlfile = STATICIMAGE_DIR + "/partofspeech.html"
    html_file = open(locationofhtmlfile, "w")
    html_file.write(html)
    html_file.close()

    return str(table1[0][0])
