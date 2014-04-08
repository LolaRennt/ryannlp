#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月05日 星期三 10时23分37秒

from good_turing import *

class BaseProb(object):
    """Base class, provide some basic interface"""

    def __init__(self):
        self.words = {}
        self.totle = 0.0
        self.unseen = 0

    def exists(self,key):
        return key in self.words

    def getTotle(self):
        return self.totle

    def getCount(self,key):
        if not self.exists(key):
            return self.unseen
        return self.words[key]

    def getFreq(self,key):
        return float(self.getCount(key))/self.totle

    def allItems(self):
        return self.words.keys()


class NormalProb(BaseProb):

    def add(self,key,value):
        self.words.setdefault(key,0)
        self.words[key] += value
        self.totle += value

class AddOneProb(BaseProb):

    def __init__(self):
        self.words = {}
        self.totle = 0
        self.unseen = 1

    def add(self,key,value):
        if not self.exists(key):
            self.words[key] = 1
            self.totle += 1
        self.totle += value
        self.words[key] += value

class GoodTuringProb(BaseProb):

    def __init__(self):
        self.words = {}
        self.totle = 0.0
        self.handled = False

    def add(self,key,value):
        self.words.setdefault(key,0)
        self.words[key] += value
        self.totle += value

    def get(self,key):
        if not self.handled:
            self.handled = True
            tmp,self.words = good_turing(self.d)
            self.none = tmp
        if not self.exists(key):
            return False,self.none
        return True,self.words[key]
