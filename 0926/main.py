def myfunction(msg):
    # a = 0
    # b = 10
    msg = msg
    def myfunction_inner():
        return msg
    return myfunction_inner
MSG = "Hello, World"
aaa = myfunction(MSG)
print(aaa)