#Week_2
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






     




   
    





 










  