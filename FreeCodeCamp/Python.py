'''

There are 3 types of data types 
string
interger 
boolean

'''
# String

print("Soham Sheth")

print("Jimmy \n Anderson")

string = "Virat Kohli "
string1 = "Rohit sharma"

print(string)
print(string + string1 + "are indian batting players") # concatenation 

# some functions used for strings 

'''
functions used for lower case 
string2.lower()
string2.upper()
string2.isupper()

You can use multiple funxtions together 


string.upper().isupper()

length function 
len(string2)


'''
string2 = "Sachin Tendulkar"
print(string2.lower())
print(string2.upper())
print(string2.isupper())
print(string2.upper().isupper())
print(len(string2))

# you can specify the index of the string and get that string out 

string3 = "Indian Cricket Team"

print(string3[0])
print(string3[4])

'''
Passing a parameter to a function. 

string3.index("C")

this will return the index of capital C
'''

print(string3.index("C"))

print(string3.index("Cric"))# this will give the index where C is getting started 

#suppose you try passing a parameter to the fuinction and try finding the index of that character which was 
# never present you will always get a error 

#print(string3.index("Z") )
print("The above statement is a error statement above")
'''
replace function 

'''
print(string3.replace("Cricket","Football"))

#Working with numbers in python 
'''
One of the most common data type is number in python

'''

print(2)
print(2.3)
print(-2.0)

#arthematic operations 


# addition , sub , multi , dvision , parathesis, square , modulous

print(1+2)
print(2-1)
print(3*4, 12/2, 12%2, 13//2, 2**2)


my_num = 34 

print(my_num)

#if you want to print string next to num use string function to convert make datatypes same

print(str(my_num)+ "string concatedation adding this sentence")

'''
Common functions related to number which you would use in day to day life 

'''

# abs = absolute value of the number

num1 = -1 
print(abs(num1))

#power functon 3**2 

print(pow(3,2))

#max function 

print(max(99,3))

#min function 
print(min(99,3))

# round function 

print(round(3.77))
print(round(4.01))
print(round(3.5))
print(round(3.49))


'''
IMPORT 
#IMPORT MATH FUNCTION 
from math import *

'''

from math import *

print(ceil(3.7))
print(floor(3.7))
print(sqrt(36))

'''
Getting input from user 
'''


#name = input("Enter you name")
#age = int(input("Enter your age "))
#printa("Hello this is " +  name + " and his age is " + str(age))

#LISTS

friends = ["sahil", "naman","ragav"]

# Lists can store diffrent datatypes 

array_aka_list = ["soham", 2 , True, "raman" , "karen"]

print(array_aka_list)
print(array_aka_list[2])
print(array_aka_list[-3])

print(array_aka_list[1:3])#this won't grab the value at index position 3 it will only grab till 2 
print(array_aka_list[-3:-1])# this again won't grab anything at index position -1
print(array_aka_list[1:5:2])# printing odd index numbers 

#changing the alue at particular index 

array_aka_list[1] = "manoj"
print(array_aka_list)



'''
LIST FUNCTIONS 

.extend
.append

'''

lucky_numbers =[2,34,66,43,21]
friend_name = ["ragav", "manpreet", "karen"]

#extend()
lucky_numbers.extend(friend_name) # extend function is extending entire list elements entire other
#where as append is creating a list also inside 
print(lucky_numbers)

lucky_numbers =[2,34,66,43,21]
lucky_numbers.append(friend_name) # append function will always append 
print(lucky_numbers)

#append()
numbers_list =[2,34,66,43,21]
numbers_list.append(5)
print(numbers_list)

#insert function 

#inserts the elemet at particular index 
#adding the element in the middle of the list

#insert()
numbers_list.insert(1,23)
print(numbers_list)

#remove()
numbers_list.remove(23)
print(numbers_list)

#clear()
numbers_list.clear()
print(numbers_list)

numbers_list =[2,34,34,66,43,21]

#pop removes last element in list 

numbers_list.pop()
print(numbers_list)

#.index()
print(numbers_list.index(34))
#print(numbers_list.index(3))#not in the list

#.count()

print(numbers_list.count(34))

#.sort()

numbers_list.sort()
print(numbers_list)
#reverse

numbers_list.reverse()
print(numbers_list)

#copy 

numbers_list_copy = numbers_list.copy()
print(numbers_list_copy)

'''

TUPLES()

'''

#tuples in python : tyuple is basically a datastructure 
# similar to list with some diffrence 

#tuple is immutable (can be changed or modified cant add , remove change any element )
#once you see it is as it is 

cooredinates = (4,5)

print(cooredinates[1])

'''

cooredinates[1]=10

can't happen because it is immutable

'''

list_of_coordinates = [(2,3),(4,5),(6,7)]
#data you dont want to change / immutable 

#FUNCTIONS
'''
FUNCTIONS 
'''
 
def sayHI(): #create a function

    print("Hi")


print("Top")
sayHI() # call a function
print("bottom")

#passing parameters 

def say_Hello(name):

    print("Hello " + name )

say_Hello("Soham")

def say_Hi_Hello(name, age ):# 2 parameters here 
    print("Hi_Hello " + name + " you age is " + age)

say_Hi_Hello("soham", "23")

say_Hi_Hello("kevin", "24")




def say_Hi_Hello(name, age ):# 2 parameters here 
    print("Hi_Hello " + name + " you age is " + str(age))

say_Hi_Hello("soham", 23)

#return statement 

def return_statement(num):

    return num*num*num 

print(return_statement(3))

def cube(num):

    return num*num*num 

result = cube(4)

print(result)

# *YOU cannot put anycode after return statement *

#IF-ELSE Statement 

is_male = True 
is_tall = False

if is_male or is_tall:
    print("The gender is male ")
elif is_male and is_tall :
    print("Surely a male ")
else :
    print("The gender is female")


# USing , function return operators and if else
    
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2 
    else :
        return num3
    
print(max_num(5,6,7))


# DICTONARIES 

# Allows us to store information in key-value pair

# you can refer any value by the key. 

'''
Program to convet 3 digit month name into whole month name 

jan --> January
feb --> february 
mar --> march


'''

# Dictonaries in python are written using {  }
#Keys always have to be unique

month_Conversions =  {

    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    0 : "January",
    1 : "February"

}

print(month_Conversions["Feb"]) #It will give me a value which is assoiated to that key

print(month_Conversions.get("Jan"))
print(month_Conversions.get("Ja")) # Good way to use get is becasuee it might happen that you dont have 
#KEY WITH THAT NAME SO YOU WOULD get reply as NONE (NOT a valid key)  instead of error
#another way


#While loops

i = 1

while i <=10:
    print(i)
    i += 1

print("while loop done ")

# Word guesser game 

secret_words = "SOHAM"
guess_words = ""
max_limit = 3
count = 0 
status = False
while guess_words != secret_words and not status:
    if count < max_limit :
        #guess_words = input("Guess the words you want to guess")
        count = count + 1
    else : 
        status = True

if status :
    print("You lost")
else :
    print("You won")



#FOR LOOP 


for i in "SOHAM SHETH":
    print(i)


friends =["soham", "sanket", "raman"]
for loss in friends :
    print(loss)

for i in range(1,11):
    print(i)

for j in range(len(friends)):
    print(j)

#EXPONENT FUNCTION 

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))
print(raise_to_power(3,3))

#2D lists and nested Loop :

number_grid = [

               [1,2,3,4],
               [2,3,4,5],
               [3,4,5,6],
               [4,5,6,7]

               ]

print(number_grid)
print(number_grid[1])

print("nested for loop")
for rows in number_grid:
    for coloumns in rows:
        print(coloumns)


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

#dog = dgg
#cat = cgg 
        
#always replace the alphabates with {AEIOUaeiou} =g 
        
def translate(phrase):
    translation = ""
    for letter in phrase :
        if letter in "AEIOUaeiou" :
            translation = translation + "g"
        else:
            translation = translation + letter 

    return translation

#print(translate(input("enter the translation")))

# comments  ; SINGLE line comment

'''
Multiple
line 
comment
'''

# TRY  and EXCEPT : if you don't want error then you can use try and expcept
# You can mention the type of error in except  which you want to print

try:
    #value = 10/0
    num = int(input("Enter the number "))
    print(num)

except ZeroDivisionError:

    print("Invalid line of code ")

except ValueError :

    print("Invalid Input ")



#READING FILES 
    


'''
Suppose there is file name employees.txt

and here you want to open file, read file, write file

then you can open file by open.txt

You can open file in couple of diffrent modes
# open("employess.txt") 
# Read : open("employess.txt", "r") : read the file
#write : open("employess.txt", "w") : change the file
# append : open("employess.txt", "a") : you can't change the any of the information you can just add append 
# Read and write : open("employess.txt", "r+") : allows us to read and write a file 

we also have a close function 
to close the file 

employee_file  = open("employess.txt")

employee_file.close()

check to make sure file is readable 

employee_file  = open("employess.txt", "r")
employee_file .readable() # true or false answer 
print(employee_file.readline())
print(employee_file.readlines()) it will take each line and out it in array format 

'''

open("employess.txt")



        


        


    
