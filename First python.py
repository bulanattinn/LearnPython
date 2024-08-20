#first python
print("Hello world")

print("Bulan Attin Nurazizah")

print(type(15))
print(type(0.5))
print(type(True))

#let's calculate how many minutes there are in 20 hours?
one_hour=60
hour=20
minutes=one_hour*hour
print(minutes)
print(type(minutes))

txt="hello {word}"
print(txt.format(word= 'World'))

#format method
message="hi, my name is {0} and i am {1} years old"
print(message.format('bulan',23))

#list
nlis=['pytho',25,2022]
print("positive and negative index of the first elemen:\n -positive index", nlis[0], "\n-negative index", nlis[1], "\n-positive index", nlis[2])



#take a list, slicing, extended the list, append()method,
text1=['Bulan',23,2024,[1,3,5,7,9,11,13],('hello', 'python', 3.14, 2023)]
len(text1)

#upper, lower, replace, split,
s1='I am learning python'
print(s1[0])
print(s1[2])

print(s1.upper())
print(s1.lower())
print(s1.replace('python', 'to code'))

s2='I am learning python'
s3='I,am,learning,python'
s4="I;am;learnig;python"
print(s2.split(" "))
print(s3.split(","))
print(s4.split(";"))


#input and output
sample = input("what is your name? :")
print( " hi " + sample + " nice to meet you")

prompt = "this is a great way to know you"
prompt += "\n now say waht is your age? "
sample = input(prompt)
print("\n you are " + sample + " years old")







