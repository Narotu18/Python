#!/usr/bin/env python
course={1:'Linux',2:'Git',3:'Vim'}

with open('./courses.data','wb') as file:    #以二进制的方式写入
	pickle.dump(course,file)

with open('./courses.data','rb') as file:    #以二进制的方式读取
	result_course=pickle.load(file)

print(result_course)
print(type(result_course))
