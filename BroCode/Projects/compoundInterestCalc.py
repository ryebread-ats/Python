#Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cant be less than or equal to zero.")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Rate cant be less than or equal to zero.")
    else:
        break
while True:
    time = int(input("Enter the time amount: "))
    if time <= 0:
        print("time cant be less than or equal to zero.")
    else:
        break
total = principle * pow((1 + rate / 100),time)
print(f"Balance after {time} years/s: ${total:.2f}")