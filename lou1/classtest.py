#!/usr/bin/env python3
class UserData:
        def __init__(self,ID,Name):
                self.ID=ID
                self.Name=Name

class NewUser(UserData):

        def __init__(self,ID,name):
                super(NewUser,self).__init__(ID,name)

        def __call__(self):                    #call函数，使实例可以被调用
                print("{}'s id is {}".format(self.Name,self.ID)) #因为是继承，要与父类的名称一致

        @property
        def name(self):
                return self.Name
        @name.setter
        def name(self,new_name):
                if isinstance(new_name,str):
                        self.__name = new_name
                else:
                        raise ValueError

        @classmethod
        def get_group(cls):
                return "shiyanlou-louplus"

        @staticmethod
        def format_userdata(id,name):
                return "%s's id is %d" %(name,id)

if __name__ == '__main__':
        user1 = NewUser(101, 'Jack')
        user2 = NewUser(102, 'Louplus')
        print("ID:{} Name:{}".format(user1.ID,user1.Name))
        print("ID:{} Name:{}".format(user2.ID,user2.Name))
        print(NewUser.get_group())
        print(NewUser.format_userdata(109,'Lucy'))
        user1.name = 'Lou'
        user1.name = 'Jackie'
        user2 = NewUser(102, 'Louplus')
        print(user1.name)
        print(user2.name)
        user = NewUser(101, 'Jack')
        user()
