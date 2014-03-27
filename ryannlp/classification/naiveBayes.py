#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月24日 星期一 20时17分21秒

import sys
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..' ))
import core.frenquency

class Bayes(object):
    
    def __init__(self):
        self.cla = {}
        self.totle  = 0

    def train(self,data):
        for d in data:
            c = d[1]
            if c not in self.cla:
                self.cla[c] = AddOneProb()
            for word in d[0]:
                self.cla[c].add(word,1)

        self.totle = sum(map(lambda x:self.cla[x].getTotle(),self.cla.keys()))

    def classify(self,data):
        tmp = {}
        for c in self.cla:
            tmp[c] = math.log(self.cla[c].totle) - math.log(self.totle)
            for word in data:
                tmp[c] += math.log(self.cla[c].getFren(word)) - math.log(self.cla[c].getTotle)

        ret,prob = 0,-1000000000

        for k in self.cla:
            if tmp[k] > prob:
                prob = tmp[k]
                ret = k

        prob = math.exp(prob)/sum(map(lambda x : math.exp(x),self.tmp))

        return ret,prob


