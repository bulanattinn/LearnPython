#if else
if 'o' in 'Python':
    print("Yes, there is 'o' in pytho")
else:
    print("Nope")



#if else multiple conditions
age = 23
member = True

if age >= 18 and member:
    print("You can vote and are a member.")
elif age >=18:
    print("You can vote but are not a member.")



#nested if -statement
score = 85
if score>=50:
    print("You passed.")
    if score >=90:
        print("Excellent")
    elif score >= 75:
        print("very good.")
    else:
        print("Good, but try to do better")
else:
    print("Sorry, you failed.")


#for range
for i in range(10):
    print(i)

for i in range(2,21,2):
    print(i)

number=87
for i in range(1,11):
    print(f"{number} X {i} = {number*i}")


#for loops(iterating over a list)
colors = ["Blue","Black",'Purple']
for color in colors:
    print(f"I like {color}")


#while loops(count down)
count = 5
while count > 0:
    print(count)
    count -=1


#list comprehensions(squerin numbers in a range)
squares = [x**2 for x in range(10)]
print(squares)

#Dictionary comprehensions
square_dict ={x: x**2 for x in range(5)}
print(square_dict)

#set comprehensions
evens = {x for x in range(10) if x % 2 == 0}
print(evens)



#break and continue
fruits=["apple","orange",'banana']
for fruit in fruits:
    if fruit=='orange':
        break
    print(fruit)

fruits=["apple","orange",'banana']
for fruit in fruits:
    if fruit=='orange':
        continue
    print(fruit)



