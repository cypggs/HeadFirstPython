#!/usr/bin/python
name = raw_input("what is your name?")

print "Hello Python!" + name + ""

#raw_input("\n\nPress the enter key to exit.")

import sys; x = 'foo'; sys.stdout.write(x + '\n')

counter = 100
mylove = "cff"

print counter
print mylove
a,b,c = 1,2,"case"

print c

s = 'ilovepython'
print s[1:5]
print s
print s[0]
print s * 2
print s + "\tTEST"

list = [ 'huihuicai', 1009, 'tianchen',25 ]
tinylist = [ 'case', 27 ]
print list
print list[0]
print list[1:3]
print tinylist * 2
print list + tinylist

tuple = ( 'ping', 23, 89 )
tinytuple = (123, 'john')
print tuple + tinytuple

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734,'dept': 'sales'}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()

x = 17
print x
y = hex(x)
print y

a = 21
b = 10
c = 0
c = a + b
print "Line 1 - Value of c is ", c
c = a - b
print c
c = a * b
print c
c = a % b
print c
c = a ** b
print c
c = a//b
print c

if ( a == b ):
	print "Line 1 - a is equal to b"
else:
	print "Line 1 - a is not wqual to b"

c = a & b;
print c
c = a | b;
print c
c = a >> 2;
print c
c = ~a;
print c
