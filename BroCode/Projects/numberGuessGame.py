import random

minNum = 1
maxNum = 100
answer = random.randint(minNum,maxNum)
print(answer)
guesses = 0
is_running = True



print("Welcome to a Python Number Guessing Game.")

while is_running:
    guess = input(f"Enter your guess from {minNum}-{maxNum}: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < minNum or guess > maxNum:
            print(f"Hey dumbass its {minNum}-{maxNum}")
        elif guess < answer:
            print("TOO LOW!!!")
        elif guess > answer:
            print("TOO HIGH!!!")
        else:
            print(f"CORRECT!!! YOU WIN!!!")
            print(f"It took you {guesses} guesses.")
            is_running = False
    else:
        print(f"Invalid number! Enter your guess from {minNum}-{maxNum}: ")
