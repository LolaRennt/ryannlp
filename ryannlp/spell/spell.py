#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月27日 星期四 20时34分23秒

import sys
import codecs
sys.path.append('../core')
import frenquency

class Spell(object):
    """This class is used for charactor to spell,and verse vas"""

    def __init__(self):
       self.chars = {}
       self.un_spell = frenquency.NormalProb()
       self.bi_spell = frenquency.NormalProb()

       self.pins = {}
       self.un_respells = frenquency.NormalProb()
       self.bi_respells = frenquency.NormalProb()

    def train(self,data):
        train_file = codecs.open(data,'r','utf-8')

        chars_queue = ['^','^']
        spell_queue = ['^','^']

        for item in train_file:
            dcorpus = item.strip().split()
            if not dcorpus:
                continue

            self.chars.setdefault(dcorpus[0],[])
            self.chars[dcorpus[0]].append(dcorpus[1])

            self.pins.setdefault(dcorpus[1],[])
            self.pins[dcorpus[1]].append(dcorpus[0])

            chars_queue.append(dcorpus[0])
            chars_queue.pop(0)
            spell_queue.append(dcorpus[1])
            spell_queue.pop(0)

            self.un_spell.add(spell_queue[1],1)
            self.bi_spells.add(tuple(spell_queue),1)

            self.un_respells.add(chars_queue[1],1)
            self.bi_respells.add(tuple(chars_queue),1)



a = Spell()
a.train('dCorpus.txt')
