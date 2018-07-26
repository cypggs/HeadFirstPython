#!/usr/bin/env python
# coding=utf-8
import random
def number_right(a,b):
    if a < b:
        print "small"
        return False
    elif a > b:
        print "big"
        return False
    else:
        print "right"
        return True
b = random.randint(1,100)
fg = False
cn = 0

while fg == False:
    a = input("please input number:")
    fg = number_right(a,b)
    cn = cn + 1
    print "cai %d" %(cn)
