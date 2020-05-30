# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:26:46 2020

@author: qtckp
"""

import codecs
import os
from textblob import TextBlob
import json


dirname = os.path.dirname(__file__)
tihu = {}


with codecs.open(os.path.join(dirname,"data/tihudict.dict"), encoding='utf-8', mode='r') as f:    
    for line in f:
        (key, val) = line.strip('\n').split('\t')
        tihu[key] = val


len(tihu)

for i, k in enumerate(tihu.keys()):
    if i % 40 ==0:
        print(str(TextBlob(k).translate(from_lang = 'fa', to = 'en')).lower(), end = ', ')



with open(os.path.join(dirname,"data/tihudict.json"), "w") as write_file:
    json.dump(tihu, write_file, indent=4)



# time 15
def read_from_dict():
    with codecs.open(os.path.join(dirname,"data/tihudict.dict"), encoding='utf-8', mode='r') as f:    
        for line in f:
            (key, val) = line.strip('\n').split('\t')
            tihu[key] = val
    return tihu

# time 3!!!!
def read_from_json():
    with open(os.path.join(dirname,"data/tihudict.json"), "r") as read_file:
        tihu = json.load(read_file)
    return tihu




with open(os.path.join(dirname,"data/tihudict.json"), "r") as read_file:
    tihu = json.load(read_file)











