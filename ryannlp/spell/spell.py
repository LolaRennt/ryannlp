#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月27日 星期四 20时34分23秒

import sys
import codecs
sys.path.append('../core')
import frenquency
import math

class Spell(object):
    """This class is used for charactor to spell,and verse vas"""

    def __init__(self):

       self.chars = {}
       self.un_spell = frenquency.AddOneProb()
       self.bi_spell = frenquency.AddOneProb()

       self.pins = {}
       self.un_respells = frenquency.AddOneProb()
       self.bi_respells = frenquency.AddOneProb()

       self.wd = frenquency.AddOneProb()

    def train(self,data):
        train_file = codecs.open(data,'r','utf-8')

        chars_queue = ['^','^']
        spell_queue = ['^','^']

        for item in train_file:
            dcorpus = item.strip().split()
            if not dcorpus:
                continue

            self.wd.add((dcorpus[0],dcorpus[1]),1)
            self.wd.add((dcorpus[1],dcorpus[0]),1)

            self.chars.setdefault(dcorpus[0],set())
            self.chars[dcorpus[0]].add(dcorpus[1])

            self.pins.setdefault(dcorpus[1],set())
            self.pins[dcorpus[1]].add(dcorpus[0])

            chars_queue.append(dcorpus[0])
            chars_queue.pop(0)

            spell_queue.append(dcorpus[1])
            spell_queue.pop(0)

            self.un_spell.add(spell_queue[1],1)
            self.bi_spell.add(tuple(spell_queue),1)

            self.un_respells.add(chars_queue[1],1)
            self.bi_respells.add(tuple(chars_queue),1)

    def decode(self,wd,hidden_set,out_set,uni_h,bi_h,string):
        """ Genereral Decode"""

        if not string:
            return
        temp = [] #Part implement

        for t in out_set[string[0]]:
            c = math.log(uni_h.getFreq(t)) + math.log(wd.getCount((string[0],t))) - math.log(uni_h.getCount(t))
            #c = math.log(wd.getCount[(string[0],t)]) - math.log(uni_h.getCount(t))
            temp.append(([t],c))

        print temp

        for ch in string[1:]:
            per_ch_temp = []
            for t in out_set.get(ch,[ch]): 
                print t
                hl  = []
                for item in temp:
                    states = list(item[0][:])
                    c = item[1]
                    print states[-1]
                    print (bi_h.getCount((states[-1],t))) ,(uni_h.getCount(states[-1])) ,(wd.getCount((ch,t))),(uni_h.getCount(t))
                    c += math.log(bi_h.getCount((states[-1],t))) - math.log(uni_h.getCount(states[-1])) + math.log(wd.getCount((ch,t))) - math.log(uni_h.getCount(t))
                    states.append(t)
                    states = tuple(states)
                    hl.append((states,c))

                hl = sorted(hl,key = lambda x :x[1],reverse = True)[0]
                per_ch_temp.append(hl)

            temp = per_ch_temp

        return " ".join(sorted(temp,key = lambda x : x[1],reverse = True)[0][0])


    def toSpell(self,data):
        return self.decode(self.wd,self.pins,self.chars,self.un_spell,self.bi_spell,data)
        pass


    def genSentence(self,data):
        return self.decode(self.wd,self.chars,self.pins,self.un_respells,self.bi_respells,data)
        pass

a = Spell()
a.train('dCorpus.txt')

