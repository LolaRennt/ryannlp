#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月13日 星期四 16时47分35秒
from __future__ import division
import math


class BM25(object):
    """This is BM25 similarity class"""
    def __init__(self,docs):

        self.d = len(docs)
        self.avgdl = sum([len(doc) for doc in docs]) / self.d
        self.docs = docs

        self.f = []# Word frenquence in every doc

        self.df = {}
        self.idf = {}

        self.k1 = 2.0
        self.b = 0.75
    
        for doc in  self.docs:
            tmp = {}
            for word in doc:
                tmp.setdefault(word,0)
                tmp[word] += 1

            self.f.append(tmp)

            for k,v in tmp.items():
                self.df.setdefault(k,0)
                self.df[k] += 1

        for k,v in self.df.items():
            self.idf[k] = math.log(self.d - v + 0.5)-math.log(v+0.5)
                
    
    def sim(self,doc,index):# The similarity between doc and docs[index]

        score = 0
        d = len(self.docs[index])

        if self.docs[index] == doc: # If is the same sentence ,then return 0, let same sentence alone
            return 0

        for word in doc:
            if word not in self.f[index]:
                continue
            score += self.idf[word] * self.f[index][word] * (self.k1 + 1) \
                    / (self.f[index][word] + self.k1 * (1-self.b+self.b*d/self.avgdl))

        return score
    

    def simall(self,doc):
        scores = []
        for index in range(self.d):
            score = self.sim(doc,index)
            scores.append(score)
        return scores

