#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ryan Liu
# Created Time : 2014年03月06日 星期四 20时04分00秒

import os
import codecs
from tnt import TnT


class Tag(object):
    """Using for tag words"""
    def __init__(self):
        self.tagger = TnT()

    def train(self,file_name):
        fr = codecs.open(file_name,'r','utf-8')
        data = []
        for i in fr:
            line = i.strip()
            if not line:
                continue
            temp = map(lambda x:x.split('/'),line.split())
            data.append(temp)
        fr.close()
        self.tagger.train(data)

