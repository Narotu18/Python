#!/usr/bin/env python3
course=[{
    'user_id': 1000,
    'name': 'Shiyan',
    'pass': 10,
    'study_time': 50,
},
{
    'user_id': 2000,
    'name': 'Lou',
    'pass': 15,
    'study_time': 171,
}]
import json

with open('/tmp/jsontest.json','w') as file:
        file.write(json.dumps(course))  #将json格式的字符串直接写入json文件  或者: json.dump(course,file)


with open('/tmp/jsontest.json','r') as file:
        result=json.load(file)

print(result)
print(result[0]['name'])
