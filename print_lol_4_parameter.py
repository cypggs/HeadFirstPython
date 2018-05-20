#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""This is movies_module"""
from __future__ import print_function
def print_lol(the_list,indent=False,level=0,fn = sys.stdout):
	"""这个函数很好用哦"""
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item,indent,level+1,fn)
		else:
			if indent:
				for tab_stop in range(level):
					print ("\t",end=' ',file = fn)
			print (each_item,file = fn)
movies = ["The Holy Grail","The LIfe of Brian","The Meaning of Life",["GC",["MP","GC","TG","EI","TJ",["haha",["i love leilei",["leilei i love you",["520 is coming",["if i tell her",["songhuo",["case so song"]]]]]]]]]]
print_lol(movies,indent=True)
