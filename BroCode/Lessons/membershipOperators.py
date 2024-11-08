#Membership operator
#used to see whether a value or variable is found in a sequence (string, list, tuple, set, dictionary)
#in
#not in
"""
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}.")
else:
    print(f"There is not a {letter}")
"""
#works the same for lists

digits = [1,2,3,4,5]

digit = 3

if digit in digits:
    print("That digit is there.")
else:
    print("That digit is not there.")

inventory = {"chairs":10,"tables":8,"desks":23}

item = "chairs"

if item in inventory:       #looks at key
    print("That item is there.")
else:
    print("That item is not there.")


findstock = 8
for item, stock in inventory.items():
    if stock == findstock:
        print(item,"-",stock)