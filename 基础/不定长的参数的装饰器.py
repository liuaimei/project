def wrapper(func):
    print("==========")
    def inner(*args,**kwargs):
        print(*args,**kwargs)
        func(*args,**kwargs)
    return  inner


@wrapper
def func(a,b,c,d):
    print(a+b+c+d)


func(7,8,9,10)