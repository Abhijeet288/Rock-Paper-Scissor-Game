import random

print("Welcome to the Game")
options=("rock","paper","scissor")
running=True

while running:
    player=None
    computer=random.choice(options)
    while player not in options:
  
        player=input("Enter your choice(rock,paper,scissor): ")
        print("Invalid input ,Try again !")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player==computer:
            print("It's a tie!")
    elif player=="rock" and computer=="scissor":
            print("You win 😁")
    elif player=="paper" and computer=="rock":
            print("You win 😁")
    elif player=="scissor" and computer=="paper":
            print("You win 😁")
    else:
            print("You loose 😢")
            
    play_again = input("Want to play agian? (y/n): ").lower()
    if not play_again=='y':
        running=False

print("Thanks for playing || Visit again !")