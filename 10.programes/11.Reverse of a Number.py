######### Reverse of a number ##########
###   Method - 1

# n = int(input("Enter number : "))
# con=str(n)
# rev=""
# for i in range (len(con)):
#     rev+=con[len(con)-i-1]
# print(rev)

# n = int(input("Enter number : "))

# rev=""

# for i in range (len(str(n))):
#     rev+=str(n)[len(str(n))-i-1]
    
# print(rev)

#### Method - 2
  ####  Using Slicing

# n = int(input("Enter number : "))
# con=str(n)
# print(con[::-1])

#### Method - 3
    ## Using While loop

# n = int(input("Enter number : "))

# rev=0
# while n!=0:
#     d=n%10
#     rev=rev*10+d
#     n//=10
# print(str(rev))  ##### this code not represent 0

# n=int(input("Enter n value:"))
# a=str(n)
# ra=0
# for i in range(len(a)):              
#     digit = n % 10
#     ra = ra * 10 + digit
#     n //= 10   
# print(ra)   ##### this code not represent 0

# n=int(input("Enter Number : "))
# rev=""
# for i in str(n):
#   rev=i+rev
# print(rev)