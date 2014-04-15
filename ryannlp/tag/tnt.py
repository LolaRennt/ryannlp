#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月05日 星期三 20时19分30秒


from __future__ import division
import sys
sys.path.append('../core')
from core import frenquency
import math

class TnT(object):
    """This is the TnT class for tagging words"""
    def __init__(self):

        self.uni = frenquency.NormalProb()
        self.big = frenquency.NormalProb()
        self.tri = frenquency.NormalProb()

        self.wd  = frenquency.AddOneProb()

        self.lam1 = self.lam2 = self.lam3 = 0

        self.state = set() #State set
        self.words = {}  #State words
        self.trans = {} # State translation prob



    def train(self,data):
        """This is the train phase ,generate the probility"""
        self.state.add(u'P')
        for sentence in data:
            tagnow = [u'P',u'P']
            sentence.append((u'EOF',u'EOF')) # Add a EOS to every sentence
            for word,tag in sentence:
                tagnow.append(tag)

                self.state.add(tag)

                self.uni.add(tag,1)
                self.big.add(tuple(tagnow[1:]),1)
                self.tri.add(tuple(tagnow[:]),1)

                self.wd.add((word,tag),1)

                self.words.setdefault(word,set())
                self.words[word].add(tag)

                tagnow = tagnow[1:]

        t1 = t2 = t3 = 0

        for item in self.tri.allItems():

            case3 = 0 if (self.big.getCount(item[:2]) - 1 ) == 0 else (self.tri.getCount(item) - 1)     / (self.big.getCount(item[:2]) - 1)

            case2 = 0 if (self.uni.getCount(item[1]) - 1)   == 0 else (self.big.getCount(item[1:]) -1 ) / (self.uni.getCount(item[1]) - 1)

            case1 = 0 if (self.uni.getTotle() - 1)          == 0 else (self.uni.getCount(item[2]) -1 )  / (self.uni.getTotle() - 1)


            if case3 >= case2 and case3 >= case1:
                t3 += self.tri.getCount(item)

            elif case2 >= case1 and case2 >= case3:
                t2 += self.tri.getCount(item)

            else:
                t1 += self.tri.getCount(item)

        self.lam1 = float(t1)/(t1+t2+t3)
        self.lam2 = float(t2)/(t1+t2+t3)
        self.lam3 = float(t3)/(t1+t2+t3)

        #print self.lam1,self.lam2,self.lam3

        for s1 in self.state:
            for s2 in self.state:
                for s3 in self.state:
                    if s3 != u'P':
                        p1 = self.lam1 * self.uni.getCount(s3) / self.uni.getTotle()
                        p2 = 0 if self.uni.getCount(s2)      == 0 else self.lam2 * self.big.getCount((s2,s3)) / self.uni.getCount(s2)
                        p3 = 0 if self.big.getCount((s1,s2)) == 0 else self.lam3 * self.tri.getCount((s1,s2,s3)) / self.big.getCount((s1,s2))

                        self.trans[(s1,s2,s3)] = math.log(p1+p2+p3)


    def tag(self,sentence):

        def not_find(c):
            if c == 0:
                return -100
            return c

        sentence.append(u'EOF')
        tagnow = [[(u'P',u'P'),0.0]]
        for word in sentence:
            #print word
            stateset = self.words.get(word,self.state)
            #print stateset
            tagpre = tagnow[:]
            tagnow = []
            for state in stateset:
                if state == u'P':
                    continue
                #print state
                tagtemp = []
                for item in tagpre:
                    tritutle = (item[0][-2],item[0][-1],state)

                    probnow = item[1]
                    probnow += self.trans[tritutle]
                    probnow += math.log(not_find(self.wd.getCount((word,state)))) - math.log(not_find(self.uni.getCount(state)))

                    statenow = list(item[0])
                    statenow.append(state)

                    tagtemp.append([tuple(statenow),probnow])
                #print tagtemp
                findmax = max(tagtemp,key=lambda x:x[1])
                tagnow.append(findmax)
        return zip(sentence,tagnow[0][0][2:-1])

