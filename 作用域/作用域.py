def test1():
    num = 200
    def test2():
        num = 100
        print(num)
    return  test2


ret = test1()
ret()