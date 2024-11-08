#Shppoing Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(f"{food : <10}", end = " ")
    for price in prices:
        print(f"{price : >10.2f}")  #f-string with 2 format specifiers: [align] and [.precision]
        total += price

print(f"Your total is: ${total :.2f}")