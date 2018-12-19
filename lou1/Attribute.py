#!/usr/bin/env python3
class Animal(object):
        def __init__(self,name,gender):
                self.name=name
                self.gender=gender
        def __getattribute__(self,attr):
                print('Get the __getattribute__ function,{}'.format(attr))
                if attr in ('name','gender'):
                        return object.__getattribute__(self,attr)
                else:
                        print('Let __getattr__ slove...')
                        return object.__getattr__(self,attr)
        def __getattr__(self,attr):
                print('Get the __getattr__ function,{}'.format(attr))
                if attr == 'age':
                        return 3
                else:
                        return "__getattr__ no attr"
dog=Animal('wangcai','male')
print(dog.name)
print(dog.age)
