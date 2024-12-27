"""
所有逻辑层模块放在此包下
"""
from lanpy.proto import Action


def who(obj: Action):
    obj.sing()
    obj.running()