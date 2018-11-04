import  types
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def run(self):
    print("===========")


def eat(self):
    print("------------")

A = Person("a",20)
print(getattr(A,"age"))
setattr(A,"city","anhui")
print(getattr(A,"city"))
print(hasattr(A,"city"))
A.run = types.MethodType(run,A)
print(A.run)
A.eat = types.MethodType(eat,A)
print(A.eat)