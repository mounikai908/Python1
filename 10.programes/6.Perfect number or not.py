# Sum of factors of given number except itself is equal to the same number
# Ex: Suppose 6 factors are 1,2,3 then 1+2+3=6

# number = int(input("Enter the number you want to know perfect or not : "))
# sum=0
# for i in range (1,number):
#     if number % i == 0:
#         sum+=i
# if sum == number :
#     print(f"The number {number} is a perfect number ")
# else:
#     print(f"The number {number} is not a perfect number")

# number=int(input("Enter number : "))

# # is_perfect=0
# perfect_num=[]
# for i in range (1,number+1):
#     per=0
#     for j in range (1,i):
#         if i % j == 0 :
#             per+=j
#     if per == i :
#         perfect_num.append(i)
        
# print(perfect_num)


### WAP to print first n numbers

# number = int(input("Enter how many prime numbers you want : "))
# num=6
# perfect=[]
# while True:
#     sum=0
#     for i in range (1,num):
#         if num % i == 0:
#             sum+=i
#     if sum == num:
#         perfect.append(num)
#     num+=1
#     if number==len(perfect):
#         break
    
# print(perfect)