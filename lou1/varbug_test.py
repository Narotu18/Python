#!/usr/bin/env python3

result = 0
start = 1
end = 100

def compute():
    global start,end,result   #引用为全局变量
    while start <= end:      #在定义之前使用变量，需要在前面定义为global;或者函数开头就定义start=*, end=*,result=*
        result += start
        start += 1
    print(result)
if __name__ == '__main__':
    compute()
