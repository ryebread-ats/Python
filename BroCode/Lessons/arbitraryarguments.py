#*args      =allows you to pass multiple non-key arguments
#**kwargs   =allows you to pass multiple keyword arguments
#           * unpacking operator before the name "args"
#1.positional 2.default 3.keyword 4.ARBITRARY

def add (*args):    #*args packs the variables into a tuple
    print(f"{type(args)}:{args}")  
    total = 0
    for arg in args:
        total += arg
    return total

add(1,2,3)
print()

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr.","John","Bob","Doe")
print()
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Street East", 
              apartment="123B",
              city="Toronto", 
              province="Ontario", 
              zipcode="Q1W74T")
print()

def shipping_label(*args,**kwargs):
    
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(f"{value}",end=" ")

shipping_label("Dr.","John","Bob","Doe",
              street="321 Street East", 
              apartment="123A",
              city="Toronto", 
              province="Ontario", 
              zipcode="Q1W74T")