# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 16:15:25 2020

@author: qtckp
"""

import requests
import time

for i in range(1,1252):
    
    url = f"http://lilak-project.com/search.php?label=V%25&page={i}"
    r = requests.get(url)
    with open(f'{i}.html', 'w', encoding = 'utf-8') as output_file:
      output_file.write(r.text)
    
    time.sleep(2)




voc = {}

for p in range(1,1252):
    
    with open(f'{p}.html', 'r', encoding = 'utf-8') as f:
      text = ''.join(f.readlines())
      
    text = (txt.strip() for txt in text.split('\n'))
    
    text = [txt for txt in text if txt.startswith('<td class=')]
    
    for i in range(int(len(text)/5)):
        
        s1 = text[5*i+1]
        s2 = text[5*i+2]
        
        i1 = s1.index('">')
        i2 = s1.index('<', i1+2)
        
        key = s1[i1+2:i2]
        key = key.replace('&jnwz;','').replace(';zwnj&','').replace('&zwnj;','')
        
        i1 = s2.index('>')
        i2 = s2.index('<', i1+1)
        
        val = s2[i1+1:i2]
        
        print(f"{key} --> {val}")
        
        if 'z' not in key:
            voc[key]=' '.join(list(val.strip()))




import json

with open('tihudict.json','r') as f:
    tihu = json.load(f)


for key in tihu.keys():
    voc[key] = tihu[key]



with open('tihudictBIG.json','w') as f:
    tihu = json.dump(voc,f, indent = 4)

























