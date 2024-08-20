import random


print("-----SIMPLE CALCULATOR-----")
print("1.+")
print("2.-")
print("3.*")
print("4./")

random.choice == int(input("Choose your operator(1,2,3,or 4) :")) 
num1 = float(input("Enter fisrt number: "))
num2 = float(input("Enter second number: "))

if random.choice == 1: 
    add = num1+num2
    print(f"{num1} + {num2} = {add}")

elif random.choice == 2: 
    sub = num1-num2
    print(f"{num1} - {num2}= {sub}")

elif random.choice  == 3:
    mul = num1*num2
    print(f"{num1} * {num2}= {mul}")

elif random.choice == 4:
    div = num1/num2
    print(f"{num1}/{num2}= {div}")

else:
    print("Invalid entry! Try entering 1,2,3,or 4!")

