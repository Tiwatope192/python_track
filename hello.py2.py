first_name = "peju"
second_name = "sokunle"
full_name = first_name + " " + second_name
print(full_name)

#F strings is used to format and build strings with variables and expressions
name = "peju sokunle"
age = 20
religion = "christianity"
is_nigerian = False
print(f"i am {name}, i am { age}, i was born a { religion} and nationality {is_nigerian}.")

#Split
dob = "1992-08-05"
print(dob.split("-"))
names = "peju tope sokunle"
print(names.split (" - "))

#string multiplier is used to repeat a value multiple times
print("peju" * 3)

#Data Extraction
#slicing and indexing
#python = 0,1,2,3,4,5, #positive indexing 
#python = -6, -5, -4, -3, -2, -1 #negative indexing
#extract the first character
text = "python"
print(text[0])
print(text[-6])
print(text[5])
print(text[-5:-3])

dob = "1992-05-08"
print(dob[1:5])
print(dob[-6:])

#strips used to remove unwanted spaces
name = " peju sokunle"
name = " peju sokunle".lstrip()
print(name)

name = "peju sokunle "
name = "peju sokunle ".rstrip()
print(name)

name = " peju sokunle "
name = " peju sokunle".strip()
print(name)

telephone = "+++490000+++"
telephone = "+++490000+++".strip("+")
print(telephone)

#To check the amount of white spaces present or unwanted char in the data
telephone = "490000"
print(len(telephone))
print(len(telephone.strip()))
print (len(telephone) == len(telephone.strip())) #“Is the string the same length before and after removing leading/trailing spaces, false means it is not clean
print (len(telephone) - len(telephone.strip()))

#case conversion
name = "peju SOKUNLE"
print(name.lower())
name = "peju SOKUNLE"
print(name.upper())

name = "Peju"
surname = "peju"
print(name == surname) #To check if the values are standardised all through
print(name.lower())
print(surname.lower())

name = "Peju".lower().strip() #cleaning the unwanted spaces and setting values to lower case
surname = "  peju".lower().strip()
print(name == surname)

#Baraa challenge
#Turn the messy string into a single clean summary with name, role and age
#"986-Maria ( D@t@ Engineer ) ;; 27y " to name: maria |role :data engineer | age: 27 and #what will be maria new age in 10 years divided by 4
raw_name = "986-Maria"
raw_role = "( D@t@ Engineer )"
raw_age = ";; 27y "
name = raw_name.replace("986-", "").strip().lower()
role = raw_role.replace("(", "").replace(")", "").replace("@", "a").strip().upper()
age = int(raw_age.replace(";", "").replace("y", "").strip())
age_in_10_years = (age + 10)
result = age_in_10_years/4
print(f"name: {name} | role: {role} | age: {age} | age_in_10_years: {age_in_10_years} | result: {result}")


#You are going to get input from a student. And then tell them their class of grade. Ensure that you are able to filter out wrong input

#3.5- 4.00 – First Class Honours
#3.0-3.49 – Second Class Honours (Upper Division)
#2.0-2.99 – Second Class Honours (Lower Division)
#1.0-1.99 – Third Class Honours
grade = input("enter your grade:")
grade = float(grade)
if grade < 1.0 or grade > 4.0:
    print("invalid grade")
elif grade >= 3.5:
    print("first class honours")
elif grade >= 3.0:
    print("second class honours upper division")
elif grade >= 2.0:
    print("second class honours lower division ")
elif grade >= 1.0:
    print("third class honours")
else: print("invalid grade")

#Write a Python program that iterates through integers from 1 to 100. For each multiple of three, print "Fizz" instead of the number; 
# for each multiple of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz"
for i in range (1,101)



#IF ELIF ELSE STATEMENTS
score = 100
if score >= 90:
    print ("A")








                

       


 

















