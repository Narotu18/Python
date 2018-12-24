#!/usr/bin/env python3
import time
from multiprocessing import Process,Value,Lock
def func(val,lock):
        for i in range(50):
                time.sleep(0.01)
		#with lock语句对下面语句的简写
                '''
                lock.acquire()
                val.value+=1
                lock.release()
                '''
		#为val变量加锁，结果就是任何时刻只有一个进程获得lock锁
		#val值不会被多个进程改变
                with lock:
                        val.value+=1
if __name__ == '__main__':
        val =Value('i',0)
        lock=Lock()
	#初始化锁
        proces=[Process(target=func,args=(val,lock)) for i in range(10)]
        for p in proces:
                p.start()
        for p in proces:
                p.join()
        print(val.value)
