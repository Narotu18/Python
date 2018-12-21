#!/usr/bin/python
#-*- coding:utf-8 -*-
import time
def chioce(func_name):
	def timer(func):
		def real_func():
			if func_name == 'task1':
				start_time=time.time()
				func()
				end_time=time.time()
				print("The %s speed %d" %(func_name,end_time-start_time))
			elif func_name == 'task2':
				start_time=time.time()
                        	func()
                        	end_time=time.time()
                        	print("The %s speed %d" %(func_name,end_time-start_time))
		return real_func
	return timer 



#@chioce(func_name='task1')
def task1():
	time.sleep(1)

#@chioce(func_name='task2')
def task2():
	time.sleep(2)

#task1()
#task2()
chioce1=chioce('task1')   # func_name == task1 , chioce1=timer函数地址
task1=chioce1(task1)     # func=task1 , task1=real_func
task1()            #real_func

chioce2=chioce('task2') #func_name == task2, chioce2=timer函数地址
task2=chioce2(task2)    #func=task2 , task2=real_func
task2()   #real_func
