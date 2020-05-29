# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:23:14 2020

@author: qtckp
"""

dataset=[
    ('سلام','salām'),
('ممنون','mamnun'),
('خب','xāb'),
('ساحل','sāhel'),
('یخ','yax'),
('لاغر','lāġar'),
('ممنون','temsāh'),
('سلام','salām'),
('ممنون','mamnun'),
('سلام','salām'),
('ممنون','mamnun'),
('سلام','salām'),
('ممنون','mamnun'),
('سلام','salām'),
('ممنون','mamnun'),
('سلام','salām'),
('ممنون','mamnun'),
('سلام','salām'),
('ممنون','mamnun'),
('سلام','salām'),
('سلام','salām'),
('سلام','salām')  ]



from PersianG2p import Persian_g2p_converter

pers = Persian_g2p_converter()

import epitran

epi = epitran.Epitran('fas-Arab')

print("""
      | persian word        | epitran convertion           | PersianG2p conversion  | expected  |
      | -------------: |:-------------:| :-----:| :-----:|""")

for p, e in dataset:
    print(f'|{p} |{epi.transliterate(p)} |{pers.transliterate(p)}| {e}|')



