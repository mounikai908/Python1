'''
1. Complex Grading System

    Write a program that takes the student's marks in multiple subjects (at least 5) as input. Based on the average of all the marks:

    If the average is greater than or equal to 90, print "A+".

    If the average is between 80 and 89 (inclusive), print "A".

    If the average is between 70 and 79 (inclusive), print "B".

    If the average is between 60 and 69 (inclusive), print "C".

    If the average is between 50 and 59 (inclusive), print "D".

    If the average is below 50, print "Fail".


    Additionally, implement a nested condition: if the student has failed any individual subject, print "Fail" even if the average is above 50.
'''
# englesh =int(input("Enter Englesh Markes : "))
# telugu = int(input("Enter Telugu Markes : "))
# mathematics = int(input("Enter Mathematics Markes : "))
# science = int(input("Enter Science Markes : "))
# social = int(input("Enter Social Markes : "))
# average_markes = int((englesh+telugu+mathematics+science+social)/5)
# if average_markes >= 90 :
#     print("congratulations your grade is A+")
# elif average_markes >= 80 and average_markes <=89 :
#     print("congratulations your grade is A")
# elif average_markes >= 70 and average_markes <=79 :
#     print("congratulations your grade is B")
# elif average_markes >= 60 and average_markes <=69 :
#     print("Congratulations your grade is C")
# elif average_markes >= 50 and average_markes <=59 :
#     print("Congratulations your grade is D")
# else :
#     print("Sorry your Fail")
'''
2. Leap Year and Century Year

    Write a program that checks if a year is a leap year or a century year:

    A year is a leap year if it is divisible by 4, but not divisible by 100 unless also divisible by 400.

    A year is a century year if it is divisible by 100 but not by 400. Based on these conditions, output:

    "Leap Year"

    "Century Year"

    "Neither Leap nor Century Year"
'''
# year = int(input("Enter Year : "))
# if ((year % 4 == 0) or (year % 400 == 0)) and (year % 100 != 0):
#     print("This is Leap Year")
# elif year % 100 == 0 and year % 400!=0 :
#     print("This is Century Year")
# else :
#     print("Neither Leap nor Century Year")

# Input: the number of primes to print
n = 10  # Change this value to print a different number of primes

count = 0  # To count the number of primes found
num = 2  # Starting number to check for primality

# # Use a for loop to find and print primes
# for _ in range(n):
#     # Check if the current number is prime
#     for i in range(2, num):
#         if num % i == 0:
#             break  # If divisible by any number, it's not prime
#     else:
#         print(num, end=" ")  # If prime, print the number
#         count += 1  # Increment the count of found primes
#     num += 1  # Move to the next number

# i = 0
# j = int(input("Enter how many prime numbers you required : "))
# is_prime = 2
# mani=[]
# while i < j :
#     counts = 0
#     for a in range (1,is_prime+1):
#         if is_prime % a == 0 :
#             counts+=1
#     if counts == 2 :
#         mani.append(is_prime)
#         i+=1
#     is_prime+=1
# print(mani)

# number=input("Enter number : ") # take input from user 

# sum_of=0

# for i in number: # loop run for every number enter in to the inner loop 
#     fac=1
#     for j in range (1,(int(i)+1)): # this loop run for 1 to i value
        
#         fac*=j #
        
#     sum_of+=fac
    
# if sum_of==int(number): # check is given number is strong number or not
#     print("This is strong number")
# else:
#     print("This is not a strong number")


#######Calculator Program############
# This function adds two numbers
# def add(x, y):
#     return x + y

# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y

# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y

# # This function divides two numbers
# def divide(x, y):
#     return x / y


# print("Select operation.")
# print("+.Add")
# print("-.Subtract")
# print("*.Multiply")
# print("/.Divide")

# while True:
#     # take input from the user
#     choice = input("Enter choice(+,-,*,/): ")

#     # check if choice is one of the four options
#     if choice in ('+', '-', '*', '/'):
#         try:
#             num1 = int(input("Enter first number: "))
#             num2 = int(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == '+':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '-':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '*':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '/':
#             print(num1, "/", num2, "=", divide(num1, num2))
        
#         # check if user wants another calculation
#         # break the while loop if answer is no
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
#     else:
#         print("Invalid Input")
