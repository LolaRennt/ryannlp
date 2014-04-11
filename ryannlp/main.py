#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月27日 星期四 09时36分02秒
import spell.spell
from spell import *

import seg.seg
from seg import *

class RyanNLP(object):
    """This is the basic class, combine all the functions using
    in Chinese language processing"""

    def __init__(self,docs):
        self.docs = docs;

        self.spe = spell.Spell()

        self.segger = seg.Seg()

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
        return self.spe.toSpell(self.docs)
        pass

    @property
    def gen(self):
        try:
            self.docs = self.docs.strip().split()
        except:
            pass
        return self.spe.genSentence(self.docs)
        pass

    @property
    def seg(self):
        return self.segger.segger.seg(self.docs)
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

    def train(self):
        #self.spe.train('spell/dCorpus.txt')
        self.segger.train('seg/data.txt')
        pass



if __name__ == "__main__":
    
    m = RyanNLP(u"本条目當前的標題「繁体中文」為暫定名稱，可能為原創、不准确或者具爭議性。 ... 注意：本條目可能有部分字元無法顯示，")
    st =  m.simp
    print st

    m.setMeta(list(u"大家新年快乐"))

    print m.seg

