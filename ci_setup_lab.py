#!/usr/bin/env python

import sys
import os, errno

"""
Set up the payu lab and input directories before running tests. 
"""

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def main():

    mkdir_p('lab/archive')
    mkdir_p('lab/bin')
    mkdir_p('lab/codebase')

    os.symlink('/short/v45/nah599/access/input', 'lab/input')

if __name__ == '__main__':
    sys.exit(main())
