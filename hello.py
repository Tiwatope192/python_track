print("cheers to writing my first code on here") #"print is a command that outputs text to the screen", single quote ' can also be used

#This is a comment, python does not execute comments

print("hello \"Everyone\"") #This command \" is an escape sequence that allows you to use double quotes inside a string

print("peju\n") #\n is an escape sequence that creates a new line

print("sokunle")

print("peju\nsokunle") #This will print peju and sokunle on different lines 

print("python basics\ndata engineering\nai")

print("my full name is:\n\t-peju\n\t-tiwatope\n\t-sokunle") #\t is an escape sequence that adds a tab space

print("""my full name is:
      \t-peju
      \t-tiwatope
      \t-sokunle""") #triple quotes can be used to create multi-line strings without the need for escape sequences to ensure readability

#OtherDataTypes
# a  = None None type
# b ="" string type
# c =" " string type emptyspace

      #Variables are used to store data values
name = "peju sokunle"   #string variable
age = "25" #string variable 
address = "lagos, nigeria"  #string variable
height = 5.6  #float variable
is_student = True  #boolean variable
religion = "Christianity"  #string variable
print(name),print(age),print(address),print(height),print(is_student),print(religion) #printing multiple variables
print(name, age, address, height, is_student, religion) #printing multiple variables in a single print statement   

x = 10  #integer variable
y = 20  #integer variable
sum = x + y  #adding two integer variables  
print("the sum of", x, "and", y, "is", sum)  #printing the sum of two integer variables

#Question 1 
name = "peju sokunle"
greet = "Good evening ahmed"
print("Good evening ahmed, my name is", name)
#Question 2
name = "peju sokunle"
age = 20
print("Hello, my name is", name, "and I am", age, "years old.")
new_age = age + 20
print("good evening ahmed, in 20 years I will be", new_age, "years old.")

#Input function allows you to take input from the user
#Static values are values that do not change, while dynamic values are values that can change based on user input or other factors.
input("enter your name:")
name = input("enter your name") #input is stored in a variable
print("you are", name)
#("enter your name") is a dynamic value, it is the data entered by the user and varies each time it runs
country = "germany" #germany is a static value, it remains same untill it is changed manually
religion = "christian"
print(name, "comes from", country, "i am a", religion)

#Class Test 1: Write a simple python code, that takes the name of a person as an input, then it greets the person

name = input("enter your name:")
greetings = "hope you are fine today."
print("hello", name, greetings)

#Class Test 2:Write a simple code that takes the name of a person as an input, takes age, welcome the person and their age plus 20
name = input("enter your name:")
age = int(input("enter your age:"))
new_age = age + 20
greetings = "hope you are fine, in 20 years you will be"
print(name, greetings, new_age )

#Type Function is used to determine the data type of a variable
text = "peju"
number = 20
print(len(text))
#print(len(number)) only works for strings

print(type(text))
print(type(number))

print(text.upper()) # changes only strings to uppercase
print(number.bit_length()) #bit_length shows how many binary digits the number have

#Episode challenge
#create 5 variables each with a different datatype
#your age, your height, your name, are you a student, something with no value yet
name = input("enter your name:")
height = float(input("enter your height:"))
age = int(input("enter your age:"))
is_student = True
future_goals = None
print(name, height, age, is_student, future_goals) #output is tuple, collection of values
print(type((name)))
#print(type(height)) age, is_student, future_goals) # not possible, eaxh line must be executed separately
print(type(age))
print(type(is_student))
print(type(future_goals))
age = 18
print(type(age))

name = "peju"
print(name)

age = 25
print(type(age))

 #len is used to count the number of characters in a string and to set conditions to conform to char length
password = "12345ab"
len(password)
print(len(password))
if len(password) < 8:
    print("your password is incorrect!")
    #len is used to count the number of characters in a string and to set conditions to conform to char length

    #count the number of time a value appears and to check the quality for any outlier
text = """
peju is a fine girl
peju is so fine
a fine girl called peju
"""
text.count("peju")
print(text.count("peju"))

#To also detect if a value is missing or present
text = """
peju is a fine girl
peju is so fine
a fine girl called peju
does she have two peju?
"""
text.count("peju")
print(text.count("sokunle"))

#Replace is used for transformation, to replace one value in a line of code with another-
phonenumber = "123-456-789"
print(phonenumber.replace ("-", "/"))

#you can also replace with nothing e.g to take out chracters
phonenumber = "123-456-789"
print(phonenumber.replace ("-", ""))

#multiple values can also be replaced
price = "£2000,56"
print(price.replace("£", "$").replace(",", "."))

#Class Challenge
#transform phone number from +49 (176) 123-4567" to 00491761234567
phone = "+49 (176) 123-4567"

print(phone.replace("+", "00")    # 0049 (176) 123-4567
      
.replace(" ", "")                   # 0049(176)123-4567

.replace("(", "")                  # 0049176)123-4567

.replace(")", "")                  # 0049176123-4567

.replace("-", ""))                 # 00491761234567

#Write a Python script that prompts for a student's name and last exam grade. Add 50 to their score, and divide their score by 4. Save the result. Then print their name and their result

name = input("Enter your name:")
score = int(input("last_exam_grade:"))
new_score = (score + 50) / 4
print(name, score, new_score)

#Concatination
first_name = "peju"
second_name = "sokunle"
full_name = first_name + " " + second_name
print(full_name)
































