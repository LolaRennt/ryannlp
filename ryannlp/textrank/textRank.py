#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月19日 星期三 09时19分06秒
import sys
sys.path.append('../sim')
import BM25

class TextRank(object):

    def __init__(self,docs):

        self.docs = docs
        self.bm25 = BM25(docs)
        self.D = len(docs)
        self.d = 0.85
        self.weight = []
        self.vertex = []
        self.max_iter = 200
        self.threshold = 0.0001
        self.top = []

    def solve(self):

        for doc in self.docs:
            scores = self.bm25.simall(doc)
            self.weight.append(scores)
            self.weight_sum.append(sum(scores))
            self.vertext.append(1.0)# Default value in 1

        for _ in range(self.max_iter):

            max_diff = 0
            new_weigh = []

            for i in range(self.D):
                new_weigh.append(1-self.d)
                for j in range(self.D):
                    if i == j or self.weight_sum[j] == 0:
                        continue
                    new_weight[-1] += self.d*self.weight[j][i]*self.vertex[j] / self.weight_sum[j] 

                max_diff = max(abs(new_weigh[-1]-self.vertex[i]),max_diff)

            self.vertex = new_weigh

            if max_diff <= self.min_diff:
                break;

        self.top = list(enumerate(self.vertex))
        self.top = sorted(self.top,key=lambda x : x[1],reverse=True)


    def get_top(self,limit=10):
        return list(map(lambda x : self.docs[x[0]],self.top[:limit]))




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
                self.vertext.setdefault(word,1.0)
                word_window.append(word) # Not exactly,if we filter according to part of speech tag ,we can get better result
                
                word_window.pop(0) if len(word_window) > co_occour

                for word_pre in word_window[:-2]: # For every words new come to word window add connection to every word in wordwindow and this word to every word
                    self.words[word_pre].add(word)
                    self.words[word].add(word_pre)


        for _ in range(self.max_iter):

            m = {} 
            max_diff = 0

            for k,v in self.words.items():
                m[k] = 1-self.d
                for j in v :
                    if k == j or len(self.word[j]) == 0:
                        continue
                    m[k] += self.d/len(self.words[j])*self.vertex[j])

                max_diff = max(abs(m[k] - self.vertex[k]),max_diff)

            self.vertex = m
            if max_diff < diff.min_diff
                break

        self.top = list(self.vertex.items())
        self.top = sorted(self.top,key=lambda x :x[1],reverse = True)

    def get_top(self,limit = 5):
        return list(map(lambda x : x[0],self.top[:limit]))




