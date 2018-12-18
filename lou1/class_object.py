#!/usr/bin/env python3
# 不同于 Java 或者 C++，Python 没有特定的关键字声明私有属性
# Python 的私有属性用一个或两个下划线开头表示
# 一个下划线表示外部调用者不应该直接调用这个属性，但还是可以调用到
# 两个下划线外部就不能直接调用到了
class Dog(object):
        def __init__(self,name):
                self.__name=name
        def get_name(self):
                return self.__name.lower().capitalize()   #可以通过函数方法对类属性二次操作
        def set_name(self,value):
                self._name = value
        def bark(self):
                print(self.get_name() + 'is making sound wang wang wnag...')

class Cat(object):
        def __init__(self,name):
                self._name = name
        def get_name(self):
                return self._name
        def set_name(self,value):
                self._name = value
        def new(self):
                print(self.get_name() + 'is making sound miu miu miu...')

dog=Dog('Wangcai')
cat=Cat('kitty')
#print(dog.__name)      #由于name是类中的私有属性；所以无法从外部调用（只有同一个类中方法函数可以调用，以此间接获取)
print(cat._name)   #name只有一个下划线的私有属性，不建议调用但依然可以获取
dog.bark()
cat.new()
