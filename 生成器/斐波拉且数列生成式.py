def fib(times):
    n = 0
    a,b = 0,1
    while n <times:
        print(b)
        a,b = b,a+b
        n = n+1
        return "done"

fib(6)