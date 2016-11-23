# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 21:57:45 2016

@author: pc
"""

import re

test = input('input the birth day like 19880101:\n')
if re.match(r'[1-2][0-9]{3}[0-1][0-9][0-3][0-9]',test):
    print('ok')
else:
    print ('falese')