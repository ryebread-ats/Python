#List Comprehension
#A concise way to create lists in python
#Compact and easier to read than traditional loops
#[expression for value in iterable if condition]
"""
doubles = []

for x in range(1,11):
    doubles.append(x * 2)
print(doubles)

doubles = [x * 2 for x in range(1,11)]
print(doubles)
"""
#both of these blocks of code do the same thing
"""
doubles = [x*2 for x in range(1,11)]
triples = [y*3 for y in range(1,11)]
squares = [z*z for z in range(1,11)]

print(doubles)
print(triples)
print(squares)
"""
"""
fruits = ["apple","orange","banana","coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits) 
"""
"""
fruits = ["apple","orange","banana","coconut"]
fruitChars = [fruit[0].upper() for fruit in fruits]
print(fruitChars)
"""
"""
numbers = [1,-2,3,-4,5,-6,7,-8,9,-10]
pos_numbers = [num for num in numbers if num >= 0]
print(pos_numbers)
neg_numbers = [num for num in numbers if num < 0]
print(neg_numbers)
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
odd_numbers = [num for num in numbers if num % 2 == 1]
print(odd_numbers)
"""


grades = [85,42,79,90,56,61,30]
passing_grades = [grade for grade in grades if grade >=60]
print(passing_grades)