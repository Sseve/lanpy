"""
entry point
"""
from lanpy.impl import Person
from lanpy.impl import Animal
from lanpy.service import who


def main():
    p = Person("zhangsan")
    a = Animal("xiaomaomi")

    who(p)
    who(a)


if __name__ == '__main__':
    main()
