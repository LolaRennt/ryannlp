# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import os
import codecs

simp_dict = {}
comp_dict = {}
charactor_dict = {}

cha_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'han.txt')
pin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'pin.txt')

file_cha = codecs.open(cha_path,'r','utf-8')
file_pin = codecs.open(pin_path,'r','utf-8')


for file_line in file_cha:
    file_line = file_line.strip()
    if not file_line:
        continue
    word_pair = file_line.split(' ')
    for item in word_pair[1]:
        if item != word_pair[0]:
            simp_dict[word_pair[0]] = item
        comp_dict[item] = word_pair[0]

file_cha.close()

for file_line in file_pin:
    file_line = file_line.strip()
    word_pair = file_line.split("=>")
    word_pair[0] = word_pair[0].strip()
    word_pair[1] = word_pair[1].strip("',")[2:]

    for item in word_pair[1]:
        charactor_dict.setdefault(item,[])
        charactor_dict[item].append(word_pair[0])

file_pin.close()

def toSimple(data):
    str = ""
    for i in xrange(0,len(data)):
        if data[i] in comp_dict:
            str += comp_dict[data[i]]
        else:
            str += data[i]

    return str



def toComple(data):
    str = ""
    for i in xrange(0,len(data)):
        if data[i] in simp_dict:
            str += simp_dict[data[i]]
        else:
            str += data[i]

    return str

