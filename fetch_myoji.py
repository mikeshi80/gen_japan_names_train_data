#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests


names = set()

for i in range(80):
    resp = requests.get('https://myoji-yurai.net/prefectureRanking.htm?prefecture=%E5%85%A8%E5%9B%BD&page={}'.format(i))
    soup = BeautifulSoup(resp.text)
    names.update([a.text for a in soup.select('div.post tr.odd a')])

with open('jpn_family_names.txt', 'w', encoding='utf8') as w:
    w.writelines('\n'.join(names))
