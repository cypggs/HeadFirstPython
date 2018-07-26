#!/usr/bin/python
a = raw_input('input a:')
b = raw_input('unput b:')
def printMax(a,b):
	if a > b:
		print a, 'is maximum'
	elif a == b:
		print 'a is equal b'
	else:
		print b, 'is maximum'
printMax(3,4)
printMax(3,3)
printMax(a,b)
