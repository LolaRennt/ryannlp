#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月27日 星期四 09时36分02秒
from spell import *

for keys in charactor_dict:
    print keys,charactor_dict[keys]


class RyanNLP(object):
    """This is the basic class, combine all the functions using
    in Chinese language processing"""

    def __init__(self,docs):
        self.docs = docs;

    @property
    def simp(self):
        pass

    @property
    def comp(self):
        pass

    @property
    def spell(self):#Spell the Chinese words
        pass

    @property
    def gen(self):
        pass

    @property
    def seg(self):
        pass

    @property
    def tag(self):
        pass

    def extractWord(self,num=1):
        pass

    def extractSentence(self,num=1):
        pass

    @property
    def classfication(self):
        pass

    @property
    def sentiment(self):
        pass

    def train(self,train_type,data):
        pass

