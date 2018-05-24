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
class Athlete:
	def __init__(self,a_name,a_dob=None,a_times =[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times
	def top3(self):
		return(sorted(set([sanitize(t) for t in self.times]))[0:3])

def openfile(file):
	try:
		with open(file) as f:
			data = f.readline()
			templ=data.strip().split(',')
			#return ({'Name':templ.pop(0),
			#	 'DOB':templ.pop(0),
#
			return (Athlete(templ.pop(0),templ.pop(0),templ))
				# 'Times':str(sorted(set([sanitize(t) for t in templ]))[0:3])})
	except IOError as ioerr:
		print('File error:'+ str(ioerr))
		return(None)
sarah=openfile('sarah2.txt')
#(sarah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)
#print(sarah_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
#sarah_data = {}
#sarah_data['name'] = sarah.pop(0)
#sarah_data['dob'] = sarah.pop(0)
#sarah_data['Times'] = sarah
#print(sarah_data['name']+"'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
#print(sarah['Name']+"'s fastest times are:"+sarah['Times'])
print (sarah.name + "'s fastest times are:"+ str(sarah.top3()))
