import dictScope

s = dictScope.dictScope()
s.__init__()
##global
list = [1,2,3,4,5,6,7,8]
s.addFunctionOrGlobalVar(name = "list", value = list)
def func(x,y):
    s.addFunctionOrGlobalVar("func", func)
    s.addLocal("y",value = y , funcI = "func")
    s.addLocal("x",value = x , funcI = "func")
    ## function func
    ## block 1
    y = 1
    s.addLocal("y",value = y , funcI = "func", block="1")
    print(s.getValue("list","func", "1"))
    for i in list:
        ## block 2
        z = list
        s.addLocal("z",value = z , funcI = "func", block="2")
        y = list.pop()
        s.addLocal("y",value = y , funcI = "func", block="2")
    ## z should not been in scope
    print(s.getValue("z","func", "1"))
    return z

func(1,2)


