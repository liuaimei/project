class Person():
    __slots__ = ("name","age")  # 指定这个类只能有这两个属性
    def __init__(self,name,age):
        self.name = name
        self.age = age


P = Person("a",90)

