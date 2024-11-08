#Match Case Statement (switch)
#An alternative to using many "elif" statements
#Execute some code if a value matches a "case"
#Benefits include cleaner and syntax is more readable

"""
def day_of_week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"

day = int(input("Enter number for day 1-7: "))
print(day_of_week(day))
"""
"""
def day_of_week(day):
    match day:    
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"

day = int(input("Enter number for day 1-7: "))
print(day_of_week(day))
"""
"""
def is_weekend(day):
    match day:    
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return "Not a valid day"

day = input("Enter day: ")
if is_weekend(day):
    print("It's the weekend!")
else:
    print("It's not the weekend.")
"""

def is_weekend(day):
    match day:    
        case "Saturday" | "Sunday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False     
        case _:
            return "Not a valid day"

day = input("Enter day: ")

if is_weekend(day) == True:
    print("It's the weekend!")
elif is_weekend(day)==False:
    print("It's not the weekend.")
else:
    print(is_weekend(day)) 