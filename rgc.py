#!/usr/bin/env python -u
# -*- coding: UTF-8 -*-
"""
Usage: rgc [options]

Options:
    --version             show program's version number and exit
    -h, --help          show this help message and exit
    -f FILE, --filename=FILE
"""

import os
from rigger_code.core import *
from optparse import OptionParser

def main():
    usage = "usage: rgc [options]"
    parser = OptionParser(usage=usage,version="%prog 2.0")
    parser.add_option("-f","--filename",metavar="FILE", help="the configuration file,default /ett/rgct.ini")
    (options, args) = parser.parse_args()
    filename =  options.filename
    if(filename==None):
        print __doc__
    else:
        if os.path.exists(filename):
            core.init(filename)
            core.run()
        else:
            print "%s not exists"%(filename)

if __name__ == "__main__":
    main()
