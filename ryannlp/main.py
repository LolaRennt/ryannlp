#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月27日 星期四 09时36分02秒
import spell.spell
from spell import *

import seg.seg
from seg import *

import tag.tag
from tag import *


class RyanNLP(object):
    """This is the basic class, combine all the functions using
    in Chinese language processing"""

    def __init__(self,docs):
        self.docs = docs;

        self.speller = spell.Spell()

        self.segger = seg.Seg()

        self.tagger = tag.Tag()

        self.train()

    def setMeta(self,docs):
        self.docs = docs

    @property
    def simp(self):
        return toSimple(self.docs)

    @property
    def comp(self):
        return toComple(self.docs)

    @property
    def spell(self):#Spell the Chinese words
        return self.speller.toSpell(self.docs)
        pass

    @property
    def gen(self):
        try:
            self.docs = self.docs.strip().split()
        except:
            pass
        return self.speller.genSentence(self.docs)
        pass

    @property
    def seg(self):
        self.temp = self.segger.segger.seg(list(self.docs))
        return " ".join(self.temp)

    @property
    def tag(self):
        return self.tagger.tagger.tag(self.docs)
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

    def train(self):
        #self.speller.train('spell/dCorpus.txt')
        #self.segger.train('seg/data.txt')
        self.tagger.train('tag/1998011.txt')
        pass



if __name__ == "__main__":
    
    m = RyanNLP(u"本条目當前的標題「繁体中文」為暫定名稱，可能為原創、不准确或者具爭議性。 ... 注意：本條目可能有部分字元無法顯示，")
    st =  m.simp
    print st

    m.setMeta([u"我",u"爱",u"东北",u"大学"])
    print m.tag

