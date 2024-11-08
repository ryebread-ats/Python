#logical operators

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor even is still scheduled.")


temp = 28
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny.")