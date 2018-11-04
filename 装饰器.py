def func(function):
    print("----func------")
    def func_in(*args,**kwargs):
        print("==========")
        function(*args,**kwargs)

    return func_in
@func
def function(a,b):
    print(a+b)


function(1,3)