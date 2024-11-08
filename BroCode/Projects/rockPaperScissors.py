import random
options = ("rock","paper","scissors")
is_running = True

while is_running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
        if player not in options:
            print("Thats not a rock, paper, or scissor...")

    print(f"Player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("Its a tie!")
        print("Try again.")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        
    elif player == "paper" and computer == "rock":
        print("You win!")
        
    elif player == "scissors" and computer == "paper":
        print("You win!")
        
    else:
        print("You lose!")
    
    if not input("Play again? (y to continue) :").lower() == "y":
        is_running  = False