# basic list comprehension questions.

#1 Even numbers
a = [i for i in range(11) if i%2==0]
print(a)

#2 Fist letter in each word
str = "Python is nice"
b = [word[0] for word in str.split()]
print(b)

#3 square numbers

c = [i*i for i in range(1,6)]
print(c)

#4 tuples from 2 lists

a = [1,2,3] 
b = [4,5,6]
c = [(i,j) for i in a for j in b]
print(c)

#5 capitlize list of strings

a = ["python is nice" , "java is good" , "c++ is poor"]
c = [i.upper() for i in a]
print(c)

#6 capitilaize the first letter in each word in list of strings

a = ["python is nice", "java is good", "c++ is poor"]
c = [i.title() for i in a]
print(c)

# loops without using list comprehesnion and Title method

sequence = ["python is good ", "java is nice " ,"c++ is fine"]
sliced_sequence = []
for i in sequence:
    b=""
    for j in i.split():
        b = b + j.capitalize() + " "
    sliced_sequence.append(b)  
print(sliced_sequence)

# list comprehension without using title method

a = ["python is nice", "java is good", "c++ is poor"]
c = [' '.join([word.capitalize() for word in i.split()]) for i in a]
print(c)