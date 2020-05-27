# Simple persian (farsi) grapheme-to-phoneme converter

It uses [this neural net](https://github.com/AzamRabiee/Persian_G2P) to convertion persian texts (with arabic symbols) into phonemes text.

Features of farsi:

* arabic notation
* the characters have different forms depended on position into word
* verbs are at the end of sentence
* no sex
* no cases
* adjectives and definitions append to the end of nouns

## Installation
```
pip install PersianG2p
```

## Usage 

```python
from PersianG2p import Persian_g2p_converter

PersianG2Pconverter = Persian_g2p_converter()

PersianG2Pconverter.transliterate('سلام')
# 'salAm'

PersianG2Pconverter.transliterate('نه تنها یک کلمه')
# 'n o h t a n h A y e k kalame'
```
