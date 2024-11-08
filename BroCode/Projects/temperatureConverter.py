#Temperature Converter

unit = input("Which temperature unit is this in? (C or F)")
temp = float(input("Enter the temperature:"))

if unit == "C":
    temp = round((9*temp)/5+32,1)
    print(f"The tempreature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp-32)*5/9,1)
    print(f"The tempreature in Celcius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit.")