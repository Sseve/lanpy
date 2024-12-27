"""
所有实现模块放在此包下
"""
from lanpy.proto import Action


class Person(Action):
    """这是一个实现示例"""
    def __init__(self, name):
        self.name = name

    def sing(self):
        print(self.name, "is sing ...")

    def running(self):
        print(self.name, "is running ...")


class Animal(Action):
    """这是一个实现示例"""
    def __init__(self, name):
        self.name = name

    def sing(self):
        print(self.name, "is sing ...")

    def running(self):
        print(self.name, "is running ...")