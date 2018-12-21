#!/usr/bin/env python3
number1=[1,2,3,4,5,6,7,8,9,10]
#首先获取列表中的偶数
f= filter(lambda x:x%2==0,number1)
#使用map方法获取所有偶数的平方,再用list方法转换
numbers=list(map(lambda x:x**2,f))
#列表解析，过滤
result=[x**2 for i in numbers if x%2 ==0]


#字典解析
d={'a':1,'b':2,'c':3}
result={k:v**v for k,v in d.items()}

#元组拆包
t=('hello','world')
a,b=t
print('I\'m {}, I\'m {} years old.'.format(*t))
