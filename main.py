#!/usr/bin/env python
# -*- coding: utf-8 -*-

from character_conveter import chara2romaji
from romaji_converter import romaji2hiragana

# ひらがな・カタカナ・漢字・ローマ字が混ざるテスト用データ
name = "久保yuうイチ" 

# 送られてきたリクエストを全てローマ字変換
rname = chara2romaji(name)
# 一旦内容確認
print(rname)

# 全てローマ字に変換された文字列をひらがなに変換
namae = romaji2hiragana(rname)
# 結果に「さん」をつけて確認
print(namae + "さん") 