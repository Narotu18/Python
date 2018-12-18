#!/usr/bin/env python3
class Animal(object):
        def __init__(self,name):   #初始化设置名字
                self.__name=name    #设置name为一个__name的私有属性变量

        def get_name(self):         # 私有属性不允许被外部访问,通过函数方法调用
                return self.__name

        def set_name(self,new_name):  # 重命名
                self._name = new_name
        def make_sound(self):
                pass

class Dog(Animal):          #继承Animal
        def __init__(self,name,age):
                super(Dog,self).__init__(name)  #
                self.age=age
        def make_sound(self):  #重写父类的 make_sound的方法
                print(self.get_name() +" " + self.age + ' is making sound wang wang wang...')

class Cat(Animal):
        def make_sound(self):
                print(self.get_name() + ' is making sound miu miu miu...')

dog=Dog('Wangcai','20')
dog.make_sound()
cat=Cat('Kitty')
cat.make_sound()
