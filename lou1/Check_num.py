#!/usr/bin/env python3
# 检查一个字符串为数字还是字母
num = input("Enter number:")
try:
        if num.isdigit():
                new_num = int(num)
                print("INT:{0}".format(new_num))
        else:
                raise ValueError("ERROR:{0}".format(num))
except ValueError as err:
        print(err)
