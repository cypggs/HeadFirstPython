#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import sys
import pickle
man = []
other = []
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			if not each_line.find(':') == -1:
				(role,line_spoken) = each_line.split(':',1)
#去除空白符
				line_spoken = line_spoken.strip() 
				if role == 'Man':
					man.append(line_spoken)
				elif role == 'Other Man':
					other.append(line_spoken)
		except ValueError:
			print ("error")
	data.close()
except IOError:
	print ("sketch file in missing!")

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

try:
	with open("man_data.txt","wb") as man_file,open("other_date.txt","wb") as other_file:	
		pickle.dump(man,man_file)
		pickle.dump(other,other_file)
	with open("man_data.txt","rb") as man_file:
		man_list=pickle.load(man_file)
		print(man_list)
		print_lol(man_list)
except IOError as err:
	print ("File error:"+ str(err))
except pickle.PickleError as perr:
	print ("Pickling error:"+ str(perr))

