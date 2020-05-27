# Simple persian (farsi) grapheme-to-phoneme converter

It uses [this neural net](https://github.com/AzamRabiee/Persian_G2P) to convertion persian texts (with arabic symbols) to phonemes text.

## Usage 

```python
from PersianG2p import PersianG2Pconverter


PersianG2Pconverter.transliterate('سلام')
# 'salAm'

PersianG2Pconverter.transliterate('نه تنها یک کلمه')
# 'n o h t a n h A y e k kalame'
```
