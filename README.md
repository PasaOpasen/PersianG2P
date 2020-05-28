# Simple persian (farsi) grapheme-to-phoneme converter

It uses [this neural net](https://github.com/AzamRabiee/Persian_G2P) to convertion persian texts (with arabic symbols) into phonemes text.

Features of farsi:

* arabic notation
* the characters have different forms depended on position into word
* vowels are often not written but pronounced; for example:
    * سس pronounces **sos** but written **ss**
    * من pronounces **man** but written **mn**
    * سلام pronounces **salām** but written **slām**
    * شما pronounces **šomā** but written **šmā**
    * ممنون pronounces **mamnun** but written **mmnun**
* the same symbols have different pronounces: in the word مو the symbol و pronounces **u**, but in the word میوه this symbol goes after vowel and pronounces **w**
* no overlap of vowel sounds
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
