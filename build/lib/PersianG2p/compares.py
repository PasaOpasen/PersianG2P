# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:23:14 2020

@author: qtckp
"""

dataset = [  ('سلام','salām'),('ممنون','mamnun'),
           ('خب','xāb'),('ساحل','sāhel'),('یخ','yax'),('لاغر','lāġar')
           ,('پسته','peste'),('مثلث','mosles')
           ,('سال ها','sālhā'),('لذت','lezzat'),('دژ','dež'),('برف','barf'),('خدا حافظ','xodā hāfez')
           ,('دمپایی','dampāyi'),('نشستن','nešastan'),('متأسفانه','mota’assefāne')
]



from G2P import Persian_g2p_converter

pers = Persian_g2p_converter()

import epitran

epi = epitran.Epitran('fas-Arab')

print("""
      | persian word        | epitran convertion           | PersianG2p conversion  | expected  |
      | -------------: |:-------------:| :-----:| :-----:|""")

for p, e in dataset:
    print(f'|{p} |{epi.transliterate(p)} |{pers.transliterate(p)}| {e}|')



