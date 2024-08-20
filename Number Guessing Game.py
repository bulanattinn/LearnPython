import random
print("Computer: I am thinking of a number between 1 to 10, can you guess? I will give you 3 chances.")
secret_number = random.randint(1, 10)

chances=3
while chances<0:
    user_guess = int(input("Enter your Guess:"))
    if secret_number==user_guess:
        print(f"Computer: Awesome!, You got the number in just {4-chances} guess!")
    break

else:
    chances-=1
    if chances>0:
        print("Computer: No, you are wrong, try again!")
        
    else:
        print(f"Computer: All 3 chances are over. The Number that I was thinking was {secret_number}")
        
  
