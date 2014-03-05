#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月05日 星期三 10时23分37秒

from good_turing import *

class BaseProb(object):
    """This is a very base probobility class"""
    def __init__(self):
        self.words = {}
        self.totle = 0.0
        self.unseen = 0

    def exists(self,key):
        return key in self.words

    def gettotle(self):
        return self.totle

    def get(self,key):
        if not self.exists(key):
            return False,self.unseen
        return True,self.words[key]

    def freq(self,key):
        return float(self.get(key)[1])/self.total

    def totleWords(self):
        return self.words.keys()


class NormalProb(BaseProb):
    def add(self,key,value):
        if not self.exists(key):
            self.words[key] = 0
        self.words[key] += value
        self.totle += value

class AddOneProb(BaseProb):
    def __init__(self):
        self.words = {}
        self.totle = 0
        self.none = 1

    def add(self,key,value):
        self.totle += value
        if not self.exists(key):
            self.words[key] = 1
            self.totle += 1
        self.words[key] += value

class GoodTuringProb(BaseProb):
    def __init__(self):
        self.words = {}
        self.totle = 0.0
        self.handled = False
    def add(self,key,value):
        if not self.exist(key):
            self.words[key] = 0
        self.words[key] += value

    def get(self,key):
        if not self.handled:
            self.handled = True
            tmp,self.words = good_turing(self.d)
            self.none = tmp
            self.totle = sum(self.words.values())+0.0
        if not self.exists(key):
            return False,self.none
        return True,self.words[key]

