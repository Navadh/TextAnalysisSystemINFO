import nltk
import sys
import codecs
from datascience import *
import numpy as np
#import matplotlib
# matplotlib.use('Agg', warn=False)
# %matplotlib inline
# import matplotlib.pyplot as plots
# plots.style.use('fivethirtyeight')



class FreqPlotClass:

    def freqtable(self):

        all_stopwords = set(nltk.corpus.stopwords.words('english'))
        input_file = 'textfile1.txt'
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

        return self.table1