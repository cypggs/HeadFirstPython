#!/usr/bin/env python
# coding=utf-8
for i in range(0,3):
    for j in range(0,4):
        for k in range(0,5):
            print i,j,k
for i in range(0, 5):
    for j in range(0, 5):
        print '*',
    print

for i in range(0, 5):
    for j in range(0, i+1):
        print '*',
    print
j = 5
for i in range(0,5):
    for j in range(5,j-1):
            print '*', 
    print "*"
