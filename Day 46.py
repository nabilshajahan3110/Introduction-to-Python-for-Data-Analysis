# INTRODUCTION TO PYTHON FOR DATA ANALYSIS

# Write the Python code to print your name

print("Nabil Shajahan")

# Write Python code that displays the numbers from 1 to 5 as steps.

for i in range(1,6):
    print(i)

# Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.

n1 = 14
n2 = 7

print(n1,"+",n2,"=", n1+n2)
print(n1,"-",n2,"=", n1-n2)
print(n1,"*",n2,"=",n1*n2)
print(n1,"/",n2,"=",n1/n2)

# Create a function calculate_area(length, width=5) that calculates the area of a rectangle. If only the length is
# provided, the function should assume the width is 5. Show how the function behaves when called with and without
# the width argument.

def area_of_rectangle(length, width=5):
    area = length * width
    return(area)

Area_with_Width = area_of_rectangle(15,3)
print(f"The area of rectangle with length and width is {Area_with_Width} square units.")

Area_with_Default_Width = area_of_rectangle(15)
print(f"The area of rectangle with length and default width is {Area_with_Default_Width} square units.")

# Write a program that prints the numbers from 1 to 15.
# But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"

for i in range (1,16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# A certain cinema currently sells tickets for a full price of 6 pounds,
# but always sells tickets for half price to people who are less than 16 years old,
# and for a third of the price for people who are 60 years old or more.
# An example run of the program (numbers in bold are typed in by the user)
# Enter your age: 63
# Your ticket costs £2.00


age = int(input("Enter your age: "))

if age < 16:
    print("Your ticket costs GBP 3.00")
elif age < 60:
    print("Your ticket costs GBP 6.00")
else:
    print("Your ticket costs GBP 2.00")


# Create a list of 5 random numbers and print the list.

import random
l1 = [random.randint(1,50) for i in range (5)]
print(l1,type(l1))
