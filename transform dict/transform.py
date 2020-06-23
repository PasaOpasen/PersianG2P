# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:30:07 2020

@author: qtckp
"""


import pandas as pd
from textblob import TextBlob
from googletrans import Translator

translator = Translator()


df1 = pd.read_table('per_phonemic.tsv', header=None)

def trans(txt):
    try:
        res = translator.translate(txt, src='fa', dest='en').text
    except:
        res = 'CANNNNNNOT'
    return res


df1[2] = pd.Series([txt.replace('\u200c','') for txt in df1[0]])

df1[3] = pd.Series([trans(txt) for txt in df1[2]])

# ', '.join(df1[0].values)

df1.to_csv('transformed.csv')



# compare with tihu

import json

with open('tihudict.json','r') as f:
    tihu = json.load(f)


def get_unique(lst):
    r = set()
    for elem in lst:
        r = r.union(set(elem))
    return r


goal = get_unique(tihu.values())

have = get_unique(df1[4])

to_delete = have.difference(goal)


inds = [k for k in range(len(df1)) if df1.iloc[k,2] in tihu and set(df1.iloc[k,4]).intersection(to_delete) != set()]

comp = df1.iloc[inds,:]
comp['target'] = pd.Series([tihu[key] for key in comp[2]], index = comp.index)


def replacenator(text):
    from_=['ʃ','ɑː','ɒː','ɔː','tʰ','æ','ɾ','j','uː','ɣ','ʔ ','iː','d ʒ','ɪ','d͡ʒ','#','xʷ','t̪']
    to_=['S','A','A','A','t','a','r','y','A','q','','i','j','i','j','','x','t']
    for f, t in zip(from_,to_):
        text = text.replace(f,t)
    return text

df1[4] = pd.Series([replacenator(a) for a in df1[1]])













