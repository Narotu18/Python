#!/usr/bin/env python3
import threading
def hello(name):
        #get_ident()
        print('cureent sub process, ID: {}'.format(threading.get_ident()))
        print("Hello " + name)

def main():
        print('current main process, ID: {}'.format(threading.get_ident()))
        print('-----------------------------------')
        t = threading.Thread(target=hello,args=('world',))
        t.start()
        t.join()
        print('-----------------------------------')
        print('current main process, thread ID:{}'.format(threading.get_ident()))

if __name__ == '__main__':
        main()
