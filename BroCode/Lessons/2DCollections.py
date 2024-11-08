#1D lists
fruits =     ["apple","orange","banana","coconut"]
vegetables = ["celery","carrots","potatoes"]
meats =      ["chicken","fish","turkey"]
#you can think of these lists as a table when they are made into a 2D list

#2D list
#two ways to make a 3D list
groceries = [fruits, vegetables, meats]

groceries1 = [["apple","orange","banana","coconut"],
             ["celery","carrots","potatoes"],
             ["chicken","fish","turkey"]]

print(groceries[0][0], end=", ")  #prints "apple", first row first index
print(groceries[1][2])            #prints "potatoes", second row third index

print(groceries1[0][0], end=", ") #prints "apple", first row first index
print(groceries1[1][2])           #prints "potatoes", second row third index

for collection in groceries:
    print(collection)             #prints out individual lsit
    for food in collection:
        print(food, end=" ")
    print()

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for char in row:
        print(char, end=" ")
    print()