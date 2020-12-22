# Introduction

This project provides the training data for Jpanaese names' OCR model.

You can use some tools, like [text_renderer](https://github.com/oh-my-ocr/text_renderer) to generate the training
data for OCR model training.

`jyouyou_list.txt` is the commonly used Japanese characters, and `jinmeiyou_list.txt` is the Japanese characters 
which is not commonly used, but can be used in Japanese name.

`text/jpn_family_names.txt` contains 40,000 Japanese family names (myoji in Japanese), which fetched from
https://myoji-yurai.net/prefectureRanking.htm

You can use this file directly, if the website updated, you also can run `fetch_myoji.py` file to fetch new names(maybe
you need modifiy the loop numbers in case there is more names be collected).
Attention, before you run the python script, please install the required dependecies by 
```sh
pip3 install -r requirements.txt
```

`text/jpn_name_char.txt` is the combination of two files above.

`text/jpn_hiragana_char.txt` and `text/jpn_katakana_char.txt` are the hiragana and katakana characters.

# Usage

## How to use with text_renderer

Put `text/*` to `text_renderer`'s `example_data/text`, and put the `char/*` to `example_data/char` folder.

To generate the Japanese family names by EnumCorpus, and the other names by RandCorpus.

`jpn_names.py` is the reference implementation for `text_renderer`, you can modify the parameters as you wish.
