#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月27日 星期四 09时36分02秒

from __future__ import division

import spell.spell
from spell import *

import seg.seg
from seg import *

import tag.tag
from tag import *

import textrank.textrank
from textrank import *

class RyanNLP(object):
    """This is the basic class, combine all the functions using in Chinese language processing"""

    def __init__(self,text):
        """ Initial the class, should set text,speller,segger,tagger,word_ranker,text_ranker """

        self.text = text;

        self.docs = []

        self.transForm()

        self.speller = spell.Spell()

        self.segger = seg.Seg()

        self.tagger = tag.Tag()

        #self.word_ranker = textrank.KeywordTextRank(self.docs)

        #self.text_ranker = textrank.TextRank(self.docs)

        self.train()


    def __setattr__(self,name,value):
        self.__dict__[name] = value
        if name == "text": # When set a new text, should re-calculate the docs matrix
            self.__dict__[name] = value.strip()
            self.transForm()

    def transForm(self):
        self.docs = []
        for item in self.text.split("\n"):
            if item.strip() :
                self.docs.append(item.strip())

    @property
    def simp(self):
        """ Convert comple Chineses to simplified Chineses """
        return toSimple(self.text)

    @property
    def comp(self):
        """ Convert simplified Chineses to comple Chineses """
        return toComple(self.text)

    @property
    def spell(self):# Spell the Chinese sentence
        """ Spell the Chineses sentense """
        return self.speller.toSpell(self.text)
        pass

    @property
    def gen(self):# Need to imporve
        """ Generate simplified Chineses sentence from spelling """
        try:
            self.docs = self.docs.strip().split()
        except:
            pass
        return self.speller.genSentence(self.docs)
        pass


    @property
    def words(self):
        return self.split_words()

    def split_words(self,echo=True):
        """ Split words from sentence """
        seg_vec = []

        for doc in self.docs:
            temp = self.segger.segger.seg(list(doc.strip()))
            if echo:
                print  " ".join(temp)
            seg_vec.append(temp)

        return seg_vec

    @property
    def tags(self):
        """ Part-of-speech tag """
        ret_vec = []
        tag_vet = []
        
        if len(self.docs[0].split(' ') ) != 1: # They are words that segged by users
            for doc in self.docs:
                tag_vet.append(doc.strip().split())
        else:
            tag_vet = self.split_words(False)

        for item in tag_vet:
            temp = self.tagger.tagger.tag(item)
            for t in temp:
                print t[0]+"/"+t[1],
            print
            ret_vec.append(temp)
            #print ret_vec

        return ret_vec
    @property
    def keyWords(self,num=4):

        self.temp = self.split_words(False)

        self.word_ranker = textrank.KeywordTextRank(self.temp)
        self.word_ranker.solve()
        
        temp = self.word_ranker.get_top(num)
        print " ".join(temp)
        return temp

    @property
    def extractSentence(self,num=3):
        
        self.temp = self.split_words(False)

        self.text_ranker = textrank.TextRank(self.temp)
        self.text_ranker.solve()
        self.ret =  self.text_ranker.get_top(num)

        for i in xrange(num):
            print self.ret[i]

        return self.ret[:num]

        pass

    @property
    def classfication(self):
        pass

    @property
    def sentiment(self):
        pass

    def train(self):
        self.speller.train('spell/dCorpus.txt')
        self.segger.train('seg/data.txt')
        self.tagger.train('tag/1998011.txt')
        pass



if __name__ == "__main__":
    
    test = u"""自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言， 所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言， 而在于研制能有效地实现自然语言通信的计算机系统， 特别是其中的软件系统。
因而它是计算机科学的一部分。
重复完成繁重的任务。 """

    m = RyanNLP(test)

    print test

    print "------Spell----"
    print m.spell

    print "------Comple---"
    print m.comp

    print "------Segs-----"
    m.words

    print "------Tags-----"
    m.tags

    print "------keyWords-"
    m.keyWords

    print "------Abstract-"
    m.extractSentence

    print "------"

    #m.extractSentence

    #m = RyanNLP(u"ni hao bei jing")

    #print m.words
    #print m.simp

    #m.docs = m.simp
    #print m.comp

    #m.docs = u"重复的完成繁重的任务"
    #print m.spell


    #m.setMeta(u"今天天气不错，挺风和日丽的。")
    #print m.seg
    #print m.tag
