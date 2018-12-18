#!/usr/bin/env python3
import sys
output_dict = {}
#handle_data函数，添加参数到字典中
def handle_data(arg):
        output_dict[arg.split(':')[0]]=arg.split(':')[1]

#print_data函数,设置输出格式
def print_data(key,value):
        print ("ID:{0} Name:{1}".format(key,value))



if __name__ == '__main__':
        for arg in sys.argv[1:]:
                handle_data(arg)
        for key in output_dict:
                print_data(key,output_dict[key])
