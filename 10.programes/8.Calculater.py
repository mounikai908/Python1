# # print("+ means Add")
# # print("- means Sub")
# # print("* means Mult")
# # print("/ means Divi")

# # operator=input("Enter operstor : ")

# # num1=int(input("Enter number 1 : "))
# # num2=int(input("Enter number 2 : "))

# # if operator == "+":
# #     print(f"{num1} + {num2} = {num1+num2}")
# # elif operator == "-":
# #     print(f"{num1} - {num2} = {num1-num2}")
# # elif operator == "*":
# #     print(f"{num1} x {num2} = {num1*num2}")
# # elif operator == "/":
# #     print(f"{num1} / {num2} = {num1/num2}")

# ###### Calculator Program ######

# #This Funcation adds two numbers

# def add(x,y):
#     return x+y

# # This funcation subracts two numbers 

# def subtract(x,y):
#     return x-y

# # This funcation multiple two numbers

# def multiply(x,y):
#     return x*y

# # This funcation divides two numbers

# def divide(x,y):
#     return x/y

# print("Select operation.")

# print("+.Add")
# print("-.Subtract")
# print("*.Multiply")
# print("/.Divide")

#         # Take input from the user 


# # check if choice is one of the four operators 
# while True :
    
#     operator=input("Enter operator +,-,*,/ : ")
    
#     if operator in ("+","-","*","/"):
#         try:
#             num1=int(input("Enter first number : "))
#             num2=int(input("Enter second number : "))
#         except ValueError:
#             print("Invalid input.Please enter a number :")
#             continue
        
#         if operator == "+":
#             print(f"{num1} + {num2} = " ,add(num1,num2))
            
#         elif operator == "-":
#             print(f"{num1} - {num2} = ",subtract(num1,num2))
            
#         elif operator == "*":
#             print(f"{num1} x {num2} = ",multiply(num1,num2))
            
#         elif operator == "/":
#             print(f"{num1} / {num2} = ",divide(num1,num2))
            
#         # check if use want to another calculation
        
#         # break the whilw loop if answer is no 
        
#         next_calculation=input("Les's do next calculation ? (yes/no) : ")
        
#         if next_calculation == "no":
#             break
#     else:
#         print("invalid input ")
































