#!/usr/bin/env python3
class Animal(object):

# 实例调用实例,return self.xxx()
        def test1(self):
                print("This is the instance function")


# 类方法可以调用实例方法，类中的属性, 调用实例-return cls.test('') or 调用类-return cls.xx(某个属性)
        @classmethod
        def test2(cls):
                print("This is the class function")


# 静态方法，调用实例方法 return Animal.test1('')  or  调用类方法 return Animal.test2()
        @staticmethod
        def test3():
                print("This is the static class function")

	def test4()
		return test1()

# How to read instance function
animal = Animal()   #将类实例化
animal.test1()
Animal.test1('hello')

# How to read a class function
Animal.test2()

# How to read a static function
Animal.test3()
