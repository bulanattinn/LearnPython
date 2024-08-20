import random
choices = ['Rock', 'Paper', 'Scissors']
computer_choice = random.choice(choices)
user_choice = input("Enter your Choice (Rock or Paper or Scissors):")

if computer_choice == user_choice.capitalize():
    print("Draw")

elif computer_choice == "Rock" and user_choice.capitalize() == "Paper":
    print("You win!")

elif computer_choice == "Paper" and user_choice.capitalize() == "Scissors":
    print("You win!")

else:
    print("Computer Wins!")