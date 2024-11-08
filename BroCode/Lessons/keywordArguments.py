#keyword arguments
#an argument preceeded by an identifier
#helps with readability
#order of arguments doesn matter
#1.positional 2.default 3.KEYWORD 4.arbitrary

def hello(greeting,title,first,last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello","Mr.","Spongebob","Squarepants")   #positional arguments, order matters

hello(first="Spongebob",greeting="Hello",title="Mr.",last="Squarepants")    #keyword arguments, order doesnt matter

hello("Hello",first="Spongebob",title="Mr.",last="Squarepants") #positional and keyword arguments. positional arguments come first

for x in range(1,11):
    print(x,end=" ")    #end is a keyword argument
print()
print("1","2","3","4","4", sep="-") #sep is a keyword argument
print("__________")

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="+1",area=905,first=434,last=7890)
print(phone_num)