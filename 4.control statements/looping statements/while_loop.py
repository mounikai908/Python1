# while True :
#     print("True")    #infinite loop

# while False :
#     print("This is loop")
# else :
#     print("else")

# wap to  print a numbers from 1 up to n numbers

# number = int(input("Enter Number : "))

# i = 1
# while i <= number :
#     print(i)
#     i+=1

# a = int(input("Enter a Value : "))
# while a <=30 :
#     print("value of a is ",a)
#     a+=1

## write a program to print a table

# table = int(input("Enter number : "))

# i = 1
# while i <=20 :
#     print(f"{table} X {i} = {table*i}")
#     i+=1


## using else with while loop 

# number = int(input("Enter A number : "))
# while number <= 10 :
#     print(f"This is i value {i}")
#     number+=1
#     if i == 7 :
#         break
# else :
#     print("this loop is exhasted ")

## use while to print characters

# string=input("enter string : ")
# lenth = len(string)
# i=0
# while i < lenth :
#     print(f'{string[i]}')
#     i+=1

 ##write a program to print staers
 
# number = int(input("Enter A number : "))
# i = 1
# while i <= number :
#     front_space = number-i
#     print("" * front_space," *" * i)
#     i+=1
# a = 1
# while a <= number :
#     front_space = number-i
#     print("" * front_space," *" * (number-a))
#     a+=1

## write a program sum of n numbers 

# number = int(input("Enter Number : "))
# even_sum=0
# odd_sum = 0
# i=1
# while i <= number :
#     if i % 2 == 0 :
#         even_sum+=i
#     else :
#         odd_sum+=i
#     i+=1
# print(f"sum of Even numbers 1 to {number} = {even_sum}\nSum of odd numbers from 1 to {number} = {odd_sum}")


#WAP ro reap the numbers until -1 is entered also count the -ve, +ve and zero entered by users

        
# number = int(input("Enter Number : "))
# number_of_positive_numbers =0
# number_of_negative_numbers =0
# number_of_zeros_ = 0
# while number != -1 :
#     if number > 0 :
#         number_of_positive_numbers+=1
#     elif number < 0 :
#         number_of_negative_numbers+=1
#     elif number==0 :
#         number_of_zeros_+=1
#     number = int(input("Enter Number : "))
# print(f"number of positive numbers entered :{number_of_positive_numbers}\nnumber of negative numbers entered : {number_of_negative_numbers}\nnumber of zeros enterd : {number_of_zeros_}")


### sum of numbers from 1 to 100
# i=1
# sum_of = 0
# while i <= 100 :
#     sum_of+=i
#     i+=1
# print("sum of 1 to 100 : ",sum_of)

### factorial numbers from 1 to n numbers 

# number = int(input("Enter a Number : "))
# i=1
# factorial=1
# while i <= number :
#     factorial*=i
#     i+=1
# print(factorial)

###Palindrome Checker: Check if a given string is a palindrome (reads the same forwards and backwards).
# Use a while loop to compare characters from both ends of the string.

string = input("Enter String : ")
i=0
reverse_string = ""
lenth_string=len(string)
while i < lenth_string :
    reverse_string+=string[lenth_string-i-1]+" "
    i+=1
    print(reverse_string)