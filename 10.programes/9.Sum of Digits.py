#Sum of Digits Ex:1234......1+2+3+4=10

#### Method - 1 #######

# number=int(input("Enter Digite : "))

# sum=0
# for i in str(number):
#     sum+=int(i)
# print(f"Sum of digite of {number} is = {sum}" )

### Method - 2 #####

# import math

# n=int(input("Enter n value : "))
# tem=n
# sum=0

# while tem > 0:
#     r=tem%10
#     sum+=r
#     tem//=10
# # print(f"Sum of digits of {n} value is : {sum}")

# #import math function to use trunc( ) function  trunc function is used to remove decimal values in python

# print(f"Sum of digits of {n} value is: {math.trunc(sum)}")

#### Method - 3 ####

# By using funcation 

# def sum_of_Digits():
#     sum=0
#     for i in str(n):
#         sum+=int(i)
#     return sum

# n = int(input("Enter N value : "))

# print(f"Sum of digits of {n} value is : {sum_of_Digits()}")