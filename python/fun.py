#coding=utf-8
#!/usr/bin/python
 
# Function definition is here
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;
 
# Now you can call printme function
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");
#!/usr/bin/python
 
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "函数内取值: ", mylist
   return
 
# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print "函数外取值: ", mylist
