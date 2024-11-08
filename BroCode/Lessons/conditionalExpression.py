num = 6
a = 6
b = 7
age = 25
temp = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

max_num = a if a > b else b
min_num = a if a < b else b
print(f"{max_num} is the bigger number.")
print(f"{min_num} is the smaller number.")

status = "Adult" if age >= 18 else "Child"
print(status)

weather = "HOT" if temp > 25 else "COLD"
print(weather)

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)