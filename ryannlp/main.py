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

import textrank.textrank
from textrank import *


class RyanNLP(object):
    """This is the basic class, combine all the functions using
    in Chinese language processing"""
    def transForm(self):
        self.docs = []
        for item in self.text.split("\n"):
            if item.strip() :
                self.docs.append(item.strip().split())

    def __init__(self,text):

        self.text = text;
        self.docs = []

        #self.transForm()

        self.speller = spell.Spell()

        self.segger = seg.Seg()

        self.tagger = tag.Tag()

        #self.word_ranker = textrank.KeywordTextRank(self.docs)

        #self.text_ranker = textrank.TextRank(self.docs)

        self.train()


    def setText(self,text):
        self.text = text
        transForm()

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
    def words(self):
        self.temp = self.segger.segger.seg(list(self.docs))
        return " ".join(self.temp)

    @property
    def tag(self):
        self.temp = self.docs.split(' ')
        if len(self.temp) == 1:
            self.temp = self.segger.segger.seg(list(self.docs))

        return self.tagger.tagger.tag(self.temp)
        pass

    def keyWords(self,num=5):

        self.test = []                   #Construct test case for using
        self.test.append(self.text)

        self.word_ranker = textrank.KeywordTextRank(self.test)
        self.word_ranker.solve()
        return self.word_ranker.get_top(num)
        pass

    def extractSentence(self,num=1):
        
        self.temp = []

        self.text_ranker = textrank.TextRank(self.docs)
        self.text_ranker.solve()

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
        #self.tagger.train('tag/1998011.txt')
        pass



if __name__ == "__main__":
    
    test = u"""
    自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
    它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
    自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
    因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
    所以它与语言学的研究有着密切的联系，但又有重要的区别。
    自然语言处理并不是一般地研究自然语言，
    而在于研制能有效地实现自然语言通信的计算机系统，
    特别是其中的软件系统。因而它是计算机科学的一部分。
    """

    test1 = u"""
    自然 语言 处理 是 计算机 科学 领域 与 人工 智能 领域 中 的 一个 重要 方向 它 研究 能 实现 人 与 计算机 之间 用 自然 语言 进行 有效 通信 的 各种 理论 和 方法 自然 语言 处理 是 一 门融 语言 学 、 计算机 科学 、 数学 于 一体 的 科学 因此 ， 这 一 领域 的 研究 将 涉及 自然 语言 ， 即 人们 日常 使用 的 语言 所以 它 与 语言学 的 研究 有着 密切 的 联系 ， 但 又 有 重要 的 区别 自然 语言 处理 并 不 是 一般 地 研究 自然 语言 而 在于 研制 能 有效 地 实现 自然 语言 通信 的 计算机 系统 特别 是 其中 的 软件 系统 
    因而 它 是 计算机 科学 的 一 部分
    """

    m = RyanNLP(test1.split())
    print m.keyWords(9)

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

