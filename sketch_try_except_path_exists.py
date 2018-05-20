#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import os
if os.path.exists('sketch.txt'):
	data = open('sketch.txt')
	for each_line in data:
		try:
			if not each_line.find(':') == -1:
				(role,line_spoken) = each_line.split(':',1)
				print (role,end='')
				print (' said: ',end='')
				print (line_spoken,end='')
		except:
			print ("error")
	data.close()
else:
	print ("sketch file in missing!")
