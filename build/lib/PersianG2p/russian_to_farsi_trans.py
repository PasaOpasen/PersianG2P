# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:49:26 2020

@author: qtckp
"""

from textblob import TextBlob
from G2P import Persian_g2p_converter

cv = Persian_g2p_converter()

while True:
    txt = input('write russian: ')
    t2 = str(TextBlob(txt).translate(from_lang = 'ru', to = 'fa'))
    print(t2)
    print(cv.transliterate(t2))


















