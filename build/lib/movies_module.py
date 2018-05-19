#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""This is movies_module"""
def print_lol(the_list):
	"""这个函数很好用哦"""
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item)
		else:
			print each_item
