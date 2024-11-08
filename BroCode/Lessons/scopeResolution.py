#variable scope
#where a variable is visible and accessible
#scope resolution
#(LEGB) Local -> Enclose -> Global -> Built-In
"""
def func1():
    a = 1   #variable is local to the function it was called in
    print(a)

def func2():
    b = 2
    print(b)
"""

def func1():
    x = 1   #variable is local to the function it was called in
    print(x)

def func2():
    x = 2
    print(x)
func1()
func2()