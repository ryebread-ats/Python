#defualt arguments
#a default value for certain parameters. default is used when that argument is omitted
#makes your functions more flexible, reduces # of arguments
#1.positional 2.DEFAULT 3.keyword 4.arbitrary

def net_price(list_price,discount=0,tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

#print(net_price(500))  #passes through one value, the function uses assigned default values for the other variables.
#print(net_price(500,0.1))  #passes through two values, the function uses assigned default values for the other variables.
#print(net_price(500, 0.1, 0))

import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("done")

count(0, 3)

#default arguments must come after positional arguments

def count1(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("done")

count1(10)
count1(10,5)    #end is at 10, start will be at 5