#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function
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
try:
	man_file = open("man_data.txt","w+")
	other_file = open("other_data.txt","w")
	print (man,file=man_file)
	print (other,file=other_file)
	man_file.close()
	other_file.close()
except IOError:
	print('File error!')
