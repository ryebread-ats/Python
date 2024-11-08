#Iterable
#An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

numbers = [1,2,3,4,5]
digits = (1,2,3,4,5)

for number in numbers:
    print(number)

for number in reversed(numbers):
    print(number, end=" ")

for digit in digits:
    print(digit)

fruits = {"apple","orange","banana","coconut"}  #sets are unordered. order will change everytime you run the code

for fruit in fruits:
    print(fruit)