def wrapper(func):
    def inner(a,b):
        print("=========")
        func(a,b)
        print(a+b)
    return inner


@wrapper
def func(a,b):
    print("a%d,b%d"%(a,b))

func(8,9)