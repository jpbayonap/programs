def foo():
    y = 20

    w = 10

#y as a local variable
    def bar():
        global y
        y = 25
        global w
        w =  0  #doesnt work
        w =  w +5 # it works
        #as a global one

    print("Before calling bar: ", y)
    print("Calling bar now")
    print("before bar w",w)
    bar() # no change  local value is taken  outside bar
    print("After calling bar: ", y)
    print("calling bar",w)
foo()
#outside the foo figthers

print("y in main : ", y)
print("w in main",w)
# global variable inside a local scope
