# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:04:16 2020

@author: qtckp
"""

from PersianG2p import PersianG2Pconverter

if __name__ == '__main__':
    TEXT = "سلام"
    out = PersianG2Pconverter.transliterate(TEXT)
    print(out)
