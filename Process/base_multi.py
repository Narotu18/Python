#!/usr/bin/env python3
import os
from multiprocessing import Process
def hello(name):
        #os.getpid() 用来获取当前的 ID
        print('child process: {}'.format(os.getpid()))
        print('Hello' +name)

#运行一个Python程序，系统会创建一个进程来运行程序，被称为主进程或父进程

def main():
        print('parent process: {}'.format(os.getpid()))

	#Process对象创建一个子任务,系统会生成一个子进程
        p = Process(target=hello,args=('shiyanlou',))
        print('child process start')
	#启动一个子进程子任务，运行的是target指定的hello()函数代码
        p.start()
        p.join()
	#子进程完成后，继续运行主进程
        print('child process stop')
        print('parent process: {}'.format(os.getpid()))
if __name__ == '__main__':
        main()
