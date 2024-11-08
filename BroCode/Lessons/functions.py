#function
#a block of reusable code
#place () after the function name to call it

"""
def happy_birthday():
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()
"""

#passing data to a function
"""
def happy_birthday(name,age):   #def happy_birthday(parameters): order matters
    print(f"Happy birthday to {name}!")
    print(f"You are {age}!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday("Ryan",25)       #happy_birthday(arguments): order matters
"""

"""
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Bob Bobby", 202.69, "21/07")
"""
#return
#a statement used to end a function and send a result back to the caller
"""
def add(x,y):
    z = x+y
    return z

def sub(x,y):
    z = x-y
    return z

def multiply(x,y):
    z = x*y
    return z

def divide(x,y):
    z = x/y
    return z

print(add(1,2))
print(sub(1,2))
print(multiply(1,2))
print(divide(1,2))
"""

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Ryan","Stevens")
print(full_name)