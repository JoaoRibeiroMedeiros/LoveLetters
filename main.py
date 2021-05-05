
#Love letters kaggle dataset by user fillerink https://www.kaggle.com/fillerink/love-letters

import numpy as np 
import pandas as pd
from nltk.probability import FreqDist
from NLPtricks import TextProcess
from matplotlib import pyplot as plt
import pandas_bokeh
import seaborn as sns
import math

LoveLetters = TextProcess.ReadLoveLetters()
stopwords = TextProcess.ReadStopWords()
LoveTokens = TextProcess.tokenize_text(LoveLetters)
LoveTokens = TextProcess.remove_stopwords(LoveTokens, stopwords)
Fdist = FreqDist(TextProcess.get_freq_dist_list(LoveTokens))

most_common = Fdist.most_common(15)

palavras = pd.Series(data=[v for k, v in most_common], index=[k for k, v in most_common])

#palavras.plot_bokeh(kind='bar', title='Frequency Distribution', xlabel='Word', ylabel='count')

fig, ax = plt.subplots(figsize=(7,4))
colors = [ 'blue', 'purple','lightblue','lightgreen',  'lightyellow','yellow', 'pink',  'orange', 'red', 'violet']

palavras.plot(kind='barh', legend = False, ax=ax, color = colors)
ax.set_ylabel(' ')
ax.set_xlabel('Times uttered within Love Letters Dataset!')
ax.set_title('Lover\'s Words')
plt.show()





