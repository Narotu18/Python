#!/usr/bin/env python3
import sys
first_list=[]
second_list=[]
for i in sys.argv[1:]:
        if len(i) <=3:
                first_list.append(i)
        else:
                second_list.append(i)
print(' '.join(first_list))
print(' '.join(second_list))
