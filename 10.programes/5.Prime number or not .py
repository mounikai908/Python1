# Check given number is prime or not 
''' If a number is divisible bt 1 and itself is know as prime number'''

print("This program works for prime number checking")

# number = int(input("Enter a number you want to check : "))

# count=0
# for i in range (1,number+1):
#     if number % i == 0 :
#         count+=1
# if count==2:
#     print(f"The number {number} is a prime number.")
# else:
#     print(f"The number {number} is not a prime number")


#### WAP to check 1 to n prime numbers 

# number=int(input ("Enter number : "))

# for i in range(1,number+1):
#     count=0
#     for j in range (1,i+1):
#         if i % j == 0 :
#             count+=1
#     if count == 2 :
#         print(i)

#### WAP to print first n prime numbers

# number = int(input("Enter how many prime numbers you want first : "))

# nub=2 

# prime_nubs=[] # store prime numbers 

# while True :
#     count=0
#     for i in range (1,nub+1):
#         if nub % i ==0:
#             count+=1
            
#     if count==2 :
#         prime_nubs.append(nub)
#     nub+=1
    
#     if len(prime_nubs) == number:
#         break
# print(prime_nubs)