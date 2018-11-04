def wrapper(func):
    def inner():
        ret = func()
        return  ret
    return  inner



@wrapper
def func():
    print("============")
    return "a"

ret = func()
print("%s"%ret)

