#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
from multiprocessing import Process
def main(func):
        def timer():
                start_time=time.time()
                #for i in range(5):
                #       func()
                process_list = []
		#创建5个多进程任务并加入到任务列表中
                for i in range(5):
                        process_list.append(Process(target=func))
                #print(process_list)
		#此时操作系统会创建5个子进程并派出闲置CPU来运行io_task()函数
                for process in process_list:
                        process.start()
		#join方法将主进程挂起并释放CPU,直到所有子进程程序运行完毕
                for process in process_list:
                        process.join()
		#子进程运行完毕，运行以下代码
                end_time=time.time()
                print("the process speed: {}".format(end_time-start_time))
        return timer
@main
def io_task():
        time.sleep(1)
if __name__ == '__main__':
        io_task()
