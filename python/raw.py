#coding=utf-8
#!/usr/bin/python
 
str = raw_input("Enter your input: ");
print "Received input is : ", str
#!/usr/bin/python
 
# 打开一个文件
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
#!/usr/bin/python
 
# 打开一个文件
fo = open("./foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");
 
# 关闭打开的文件
fo.close()
