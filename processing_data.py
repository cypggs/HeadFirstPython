#!/usr/bin/python
# -*- coding: UTF-8 -*-
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return(mins + '.' + secs)
with open('james.txt') as jaf:
	data=jaf.readline()
	james = data.strip().split(',')
with open('julie.txt') as juf:
        data=juf.readline()
        julie = data.strip().split(',')
with open('mikey.txt') as mif:
        data=mif.readline()
        mikey = data.strip().split(',')
with open('sarah.txt') as saf:
        data=saf.readline()
        sarah = data.strip().split(',')
#通过append装换一个新列表
clean_james = []
for each_t in james:
	clean_james.append(sanitize(each_t))
print(sorted(clean_james))
#通过装换列表完成
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))
