
def function(*args):
    def wrapper(func):
        def inner():
            print("-----记录日志------%s"%args)
            func()
        return  inner
    return  wrapper


@function("haha")
def test1():
    print("-----test1-----")

@function("heihei")
def test2():
    print("------test2-----")

test1()
test2()