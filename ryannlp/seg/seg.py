#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月11日 星期二 09时43分59秒

import sys
import codecs
from cbgm import CharacterBasedGenerativeModel

class Seg(object):
    
    def __init__(self):

        self.segger = CharacterBasedGenerativeModel()

    def train(self,file_name):

        fr = codecs.open(file_name,'r','utf-8')
        data = []
        for i in fr:
            line = i.strip()
            if not line:
                continue
            tmp = map(lambda x:x.split('/'),line.split())
            data.append(tmp)
        fr.close()
        self.segger.train(data)

