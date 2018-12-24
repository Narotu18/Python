#https://docs.python.org/3.5/library/pipes.html?highlight=pipe#module-pipes
#!/usr/bin/env python3
from multiprocessing import Pipe,Process
conn1,conn2 = Pipe()

def main(func_name):
        def channel(func):
                def sed_recv():
                        if func_name == 'send':
                                Process(target=func).start()
                        elif func_name =='recv':
                                Process(target=func).start()
                return sed_recv

        return channel

@main(func_name='send')
def send():
        data='hello shiyanlou'
        conn1.send(data)
        print('Send Data:{}'.format(data))
@main(func_name='recv')
def recv():
        data=conn2.recv()
        print('Receive Data: {}'.format(data))

if __name__ == '__main__':
        send()
        recv()
