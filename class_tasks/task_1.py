#
# Task 1: Write a simple python code, that takes the name of a person as an input, then it greets the person

name = input("enter your name:")
greetings = "hope you are fine today."
print("hello", name, greetings)

# Task 2:Write a simple code that takes the name of a person as an input, takes age, welcome the person and their age plus 20
name = input("enter your name:")
age = int(input("enter your age:"))
new_age = age + 20
greetings = "hope you are fine, in 20 years you will be"
print(name, greetings, new_age )

#Week_2

#Task 1
# grade = input("enter your grade:")
grade = 1.5
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

#Task 2
#Write a Python program that iterates through integers from 1 to 100. For each multiple of three, print "Fizz" instead of the number; 
# for each multiple of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz"
#For numbers that are multiples of both three and five, print "FizzBuzz"
for integers in range(1, 101):

    if integers % 3 == 0 and integers % 5 == 0:
        print("FizzBuzz")

    elif integers % 3 == 0:
        print("Fizz")

    elif integers % 5 == 0:
        print("Buzz")

    else:
        print(integers)

sales = [120, 450, 300, 50, 800, 200]
#sales < 300 = low
#sales btwn 300 to 700 = medium
#sales higher than 700 = high
for sales in sales:
    if sales <= 300:
        category = 'low'
    elif sale <= 700:
        category = 'medium'
else:
    category = 'high'
        
        





     




   
    





 










  