'''Task 1:
Write a program that asks the user for their age and prints "You are a minor" if they are under 18,
"You are an adult" if they are 18 or older, and "You are a senior citizen" if they are 65 or older.'

age = int(input("enther age : ")) # input take 
if age < 18 :
    print("You are a minor")
elif age > 18 and age < 65 :
    print("you are an adult")
else :
    print("you are a senior citizen")

'''

'''
1. Check if a number is even or odd:

number = int(input("enter number : "))
if number % 2 == 0 :
    print("even number ")
else :
    print("odd number")
'''

'''
2. Find the largest of three numbers:

    # take the input from users 
number1 =int(input("enter number 1 : "))
number2 =int(input("enter number 2 : "))
number3 =int(input("enter number 3 : "))

#determine largest number 
if (number1 > number2) and number1 > number3 :
    print("this is largest number",(number1))
elif number2 > number3 :
    print("this is largest number",(number2))
else :
    print("this is largest number",(number3))
'''
'''
3. Positive, Negative, or Zero

    Write a program that takes a number and checks whether it is positive, negative, or zero.
    Example:
    Input: -3
    Output: Negative


    # we can take input from user
number = int(input("Enter a Number : "))

# identify the number is postive or negative or zero 
if number > 0 :
    print("This is positive number :",(number))
elif number < 0 :
    print("This is negative number : ",(number))
else :
    print("this is Zero : ",(number))
'''
'''
4.Grade Classification

    Write a program that takes a student's score and classifies it into a grade. Use the following criteria:
    90 and above → "A"
    80-89 → "B"
    70-79 → "C"
    60-69 → "D"
    Below 60 → "F"
    Example:
    Input: 85
    Output: B

    # take inpute from user 
    marks = int(input("enter the marks : "))

    # identify grade

    if marks >= 90 :
        print("you  passed your grade is : A")
    elif marks < 90 and marks >= 80 :
        print("you  passed your grade is : B")
    elif marks < 80 and marks >=70 :
        print("you  passed your grade is : C")
    elif marks < 70 and marks >= 60 :
        print("you  passed your grade is : D")
    else :
        print("your fale your grade is : F")

5. Leap Year

    Write a program to check whether a given year is a leap year.
    A year is a leap year if it is divisible by 4 but not divisible by 100, unless it is also divisible by 400.
    Example:
    Input: 2020
    Output: Leap year

        # take inptu from user 
    year = int(input("Enter year : "))
    # check year leap year or not 

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("this is leap year : ",year)
    else :
        print("this is not leap year : ",year) 

6.  Maximum of Three Numbers

    Write a program that takes three numbers as input and prints the largest number.
    Example:
    Input: 2, 8, 5
    Output: 8
    # take inputs from user
        number1 = int(input("Enter number 1 : "))
        number2 = int(input("Enter number 2 : "))
        number3 = int(input("Enter number 3 : "))

    #Identify largest number 
        if number1 > number2 and number1 > number3:
            print("this is largest number : " , number1)
        elif number2 > number3 :
            print("This is largest number : " , number2)
        else :
            print("this is largest number :" , number3)

7.Age Group Classification

    Write a program that takes an age and categorizes it as one of the following:
    Child: 0-12 years
    Teen: 13-19 years
    Adult: 20-64 years
    Senior: 65 years and above

    
    # take input from user
        age = int(input("Enter your age : "))

    # categorizes age 
        if age >= 0 and age <= 12 :
            print("you are a child")
        elif age >= 13 and age <= 19 :
            print("you are teen ager")
        elif age >= 20 and age <= 60 :
            print("your are Adult ")
        else :
            print("You are senior cetizan")


8. Divisibility Checker

    Write a program that checks if a number is divisible by 5, 10, or both, and outputs the appropriate message.
    If divisible by 5 but not 10: "Divisible by 5"
    If divisible by 10: "Divisible by 10"
    If divisible by both: "Divisible by both"
    If divisible by neither: "Not divisible by 5 or 10"
    Example:
    Input: 50
    Output: Divisible by both

    # take value from user 
        number = int(input("Enter number : "))

    # check divisiblity
        if number % 5 ==0 and number % 10 ==0 : # check the number Divisible by 5 and 10
            print("Divisible by both")
        elif number % 5 ==0 :  # check the number id divisible bye 5
            print("divisible by 5")
        elif number % 10 == 0 :  # check the number id divisible bye 10
            print("divisible by 10")
        else :
            print("Not divisible by 5 or 10 ")

9. Vowel or Consonant

    Write a program that takes a character as input and checks whether it is a vowel (a, e, i, o, u) or a consonant.
    Example:
    Input: e
    Output: Vowel

    # take input from user 
        char = input("Enter chharacter : ")
    #identify vowel or consonant
        if char in "aeiouAEIOU":
            print("Vowel") 
        else :
            print("consonant")

10.BMI Calculator

    Write a program that takes a person's weight (kg) and height (m) as inputs, calculates the BMI, and prints the classification:
    Underweight: BMI < 18.5
    Normal weight: 18.5 ≤ BMI < 24.9
    Overweight: 25 ≤ BMI < 29.9
    Obese: BMI ≥ 30
    Example:
    Input: weight = 70, height = 1.75
    Output: Normal weight

    # take inputes from user 
        weight = int(input("Enter Weight : "))
        height = float(input("Enter height : "))
        # calculate Bmi
        bmi = weight / (height **2) 

    # check the classification 
        if bmi < 18.5 :
            print("underweight")
        elif bmi >= 18.5 and bmi < 24.9 :
            print("Normal weight")
        elif bmi >= 25 and bmi < 29.9 :
            print("Overwight")
        else :
            print("obese")
11.Ticket Pricing

    Write a program that calculates the price of a movie ticket based on the age of the customer:
    Child (0-12): $5
    Teen (13-17): $7
    Adult (18-64): $10
    Senior (65+): $6
    Example:
    Input: age = 15
    output: Ticket Price: $7

    # Take input from user 
        age = int(input("Enter age : "))
        
        if age <= 12 :  # check age is between 0-12
            print("Ticket Price : $5")
        elif age >= 13 and age <=17 :  # check age is between 13-17
            print("Ticket Price : $7")
        elif age >= 18 and age <= 64 : # check age is between 18-64
            print("Ticket Price :$10")
        else :  # check age above 65+
            print("Ticket Price :$6") 

            
12 . Number Range Check

    Write a program that checks if a number falls within a given range (inclusive). For example:
    Range: 10-20
    If the number is within the range, output In Range
    If the number is outside the range, output Out of Range
    Example:
    Input: 15
    Output: In Range
    
    # take input from user
        number = int(input("Enter number : "))

        if number >= 10 and number <=20: # check given number rage between 10-20
            print("In range")
        else :
            print("Out of range")


13.Custom Time Greeting

    Write a program that asks for the current hour (in 24-hour format) and greets the user accordingly:
    0-11: Good Morning
    12-17: Good Afternoon
    18-23: Good Evening
    Example:
    Input: 13
    Output: Good Afternoon
    
    # take input from user
        time = float(input("Enter time : "))
    # greets the user
        if time <= 0 and time <= 11 :
            print("Good Morning")
        elif time <= 12 and time <= 17 :
            print("Good Afternoon")
        elif  18<= time <=23 :
         print("Good Evening")
         
'''