#!/usr/bin/python
count = 0
while (count < 9):
	print 'The count is:',count
	count = count + 1
print "Good bye!"

i = 1
while i < 10:
	i += 1
	if i%2 > 0:
		continue
	print i

i = 1
while 1:
	print i
	i += 1
	if i > 10:
		break

count = 0
while count < 5:
	print count,"is less than 5"
	count = count + 1
else:
	print count, "is not less than 5"
flag = 1
while (flag) : print 'Given flag is really true!'
print "Good bye!"

var = 1
while var == 1:
	num = raw_input("Enter a number :")
	print "You entered: ",num
print "Good bye!"
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i " 是素数"
   i = i + 1

print "Good bye!"
