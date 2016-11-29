#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser

class myConfigParser:

    config =''

    @staticmethod
    def load(filename):
        try:
            myConfigParser.config   = ConfigParser.RawConfigParser()
            myConfigParser.config.read(filename)
        except Exception,e:
            print e

    @staticmethod
    def get(section,name):
        try:
            return myConfigParser.config.get(section,name)
        except Exception,e:
            print e
