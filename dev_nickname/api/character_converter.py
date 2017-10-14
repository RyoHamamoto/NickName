#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pykakasi import kakasi

kakasi = kakasi()

def chara2romaji(text):
    global kakasi
    kakasi.setMode('H', 'a')
    kakasi.setMode('K', 'a')
    kakasi.setMode('J', 'a')
    conv = kakasi.getConverter()
    result = conv.do(text)
    return result