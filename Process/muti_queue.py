#!/usr/bin/env python3
from multiprocessing import Pipe,Process,Queue
# 创建队列实例
queue = Queue()
def main(func_name):
        def channel(func):
                def sed_recv(q):
                        if func_name == 'send':
                                Process(target=func,args=(q,)).start()
                        elif func_name =='recv':
                                Process(target=func,args=(q,)).start()
                return sed_recv

        return channel
#从队列发送数据量
@main(func_name='send')
def f1(q):
        data='hello shiyanlou'
        q.put(data)
        print('Send Data:{}'.format(data))
@main(func_name='recv')
def f2(q):
        data=q.get()
        print('Receive Data: {}'.format(data))

if __name__ == '__main__':
        f1(queue)
        f2(queue)
