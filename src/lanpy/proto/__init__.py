"""
所有协议模块放在此包下
该包下的模块依赖于proto包下的模块。即, 该包下模块中的类需要实现proto包下模块中对应的类接口
"""
from typing import Protocol


class Species(Protocol):

    def sing(self):
        ...

    def running(self):
        ...
