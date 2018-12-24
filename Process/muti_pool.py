#!/usr/bin/env python3
import os,time,random
from multiprocessing import Pool
def task(name):
        print("task{} start, processID:{}".format(name,os.getpid()))
        start=time.time()
        time.sleep(random.random() *3)
        end=time.time()
        print('task{} end, speed:{:.2f}s'.format(name,(end-start)))

if __name__ == '__main__':
        print('current main process, ID:{}'.format(os.getpid()))
        print('-----------------------------------------------')
	#创建进程池，只允许4个进程可用
        p = Pool(4)
	#添加5个任务加入到进程池
        for i in range(1,6):
		#apply_async方法异步启动进程池
		#池内进程随机接收任务,直到所有任务完成
                p.apply_async(task,args=(i,))
	#关闭进程池
        p.close()
        print("start the sub process.....")
	#join方法是先挂起主进程,直到进程池内任务完成
        p.join()
        print('---------------------------')
        print('All sub process run over, current is main process, process ID:{}'.format(os.getpid()))
