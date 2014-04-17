#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月19日 星期三 09时19分06秒

from __future__ import division
import sys
sys.path.append('../sim')
from sim import BM25

class TextRank(object):

    def __init__(self,docs):

        self.docs = docs
        self.bm25 = BM25.BM25(docs)
        self.D = len(docs) # length of all the sentence

        self.d = 0.85

        self.weight = []
        self.weight_sum = []
        self.vertex = []

        self.max_iter = 200
        self.threshold = 0.0001
        self.top = []

    def solve(self):

        for doc in self.docs:
            scores = self.bm25.simall(doc)

            self.weight.append(scores)
            self.weight_sum.append(sum(scores))
            self.vertex.append(1.0)# default value is 1

        for _ in range(self.max_iter):

            max_diff = 0
            new_weigh = []

            for i in range(self.D):
                new_weigh.append(1-self.d)
                for j in range(self.D):
                    if i == j or self.weight_sum[j] == 0:
                        continue
                    new_weigh[-1] += self.d*self.weight[j][i]*self.vertex[j] / self.weight_sum[j]

                max_diff = max(abs(new_weigh[-1]-self.vertex[i]),max_diff)

            self.vertex = new_weigh

            if max_diff <= self.threshold:
                break;

        self.top = list(enumerate(self.vertex))
        self.top = sorted(self.top,key=lambda x : x[1],reverse=True)


    def get_top(self,limit=10):
        return list(map(lambda x : "".join(self.docs[x[0]]),self.top[:limit]))




class KeywordTextRank(object):
    
    def __init__(self,docs):
        
        self.docs = docs
        self.words = {}
        self.vertex = {}
        self.d = 0.85
        self.max_iter = 200
        self.min_diff = 0.001
        self.top = []
        self.co_occour = 3

    def solve(self):

        for doc in self.docs:

            word_window = []

            for word in doc:

                self.words.setdefault(word,set())
                self.vertex.setdefault(word,1.0)

                word_window.append(word) # Not exactly,if we filter according to part of speech tag ,we can get better result
                if len(word_window) > self.co_occour:
                    word_window.pop(0)

                for word_pre in word_window[:-1]: # For every words new come to word window add connection to every word in wordwindow and this word to every word

                    self.words[word_pre].add(word)
                    self.words[word].add(word_pre)


        for _ in range(self.max_iter):

            m = {}
            max_diff = 0

            for k,v in self.words.items():
                m[k] = 1-self.d
                for j in v :
                    if k == j or len(self.words[j]) == 0:
                        continue
                    m[k] += self.d/len(self.words[j])*self.vertex[j]

                max_diff = max(abs(m[k] - self.vertex[k]),max_diff)

            self.vertex = m
            if max_diff < self.min_diff:
                break

        self.top = list(self.vertex.items())
        self.top = map(lambda x : x[0],sorted(self.top,key=lambda x :x[1],reverse = True))
        self.top = filter(lambda x : len(x)>1 ,self.top)[:5]

        self.ret_map = sorted(self.mergeWord(self.top),key = lambda x :len(x),reverse = True)
        
    def mergeWord(self,top):
        """ Merge key words according to the source sentencs"""
        word_set = set()
        for doc in self.docs:
            temp = ""
            for item in doc:
                if item in top:
                    temp += item
                else:
                    if temp:
                        word_set.add(temp)
                    temp = ""
        return word_set


    def get_top(self,limit = 5):
        return self.ret_map[:limit]

