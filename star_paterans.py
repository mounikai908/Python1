'''
Right-Angled Triangle Pattern:
*
**
***
****
*****

'''
# number = int(input("Enter number : "))
# for i in range (1,number+1):
#     print("*" * i)

'''
Inverted Right-Angled Triangle Pattern:
*****
****
***
**
*

'''
# number=int(input("Enter number : "))
# for i in range (number):
#     print("*" * (number-i))

'''
Pyramid Pattern:
    *
   ***
  *****
 *******
*********

'''
# number = int(input("Enter number : "))
# for i in range (1,number+1):
#     space = " " * (number-i)
#     print(space,"* " * i)

'''
Diamond Pattern:
    *
   ***
  *****
 *******
  *****
   ***
    *

'''
# number = int(input("Enter number : "))
# for i in range (1,number+1):
#     space = " " * (number-i)
#     print(space,"* " * i)
#     if i == number :
#         for j in range (1,number):
#             space = " " * (j)
#             print(space,"* " * (number-j))

'''
Square Pattern:
*****
*****
*****
*****
*****

'''
# number = int(input("Enter number : "))
# for i in range (number):
#     print("*" * number)

'''
Hollow Square Pattern:
*****
*   *
*   *
*   *
*****

'''
# number = int(input("Enter number : "))
# for i in range (number):
#     if i == 0 or i == (number-1):
#         print("* " * number)
#     else : 
#         space = " " * (number-2)
#         print("* ",space," *")

'''
Right-Angled Triangle with Numbers:
1
12
123
1234
12345

'''
# number = int(input("Enter number : "))
# for i in range (1,number+1):
#     row=""
#     for j in range (1,i+1):
#         row+=str(j)
#     print(row)

'''
Inverted Pyramid Pattern:
*********
 *******
  *****
   ***
    *

'''
# number=int(input("Enter number : "))
# count=[]
# a=0
# n=1
# while a < number :
#         if n % 2 !=0:
#             count.append(n)
#             a+=1
#         n+=1     
# for i in range (len(count)):
#     space= " " * (i)
#     star = "*" * count[-(i+1)]
#     print(space,star)

'''
Hollow Pyramid Pattern:
    *
   * *
  *   *
 *     *
*********

'''
# number = int(input("Enter number : "))
# for i in range (1,number+1):
#     space = " " * (number-i)
#     if i ==1 :
#         print(space,"*" * i)
#     elif i == number :
#         print(space,"*" * (number*2-1))
#     else :
#         print(space+"* "+"  "*(i-2)+" *")

'''
1
2 3
4 5 6
7 8 9 10

'''
# number = int(input("Enter number : "))
# n=1
# for i in range (1,number):
#     a=""
#     for j in range (i):
#         a+=str(n)+" "
#         n+=1
#     print(a)

'''
*********
*     *
 *   *
  * *
   *

'''
# number = int(input("Enter number : "))
# for i in range (number):
#     a= number-i
#     space=" " * (i)
#     if a == 1 :
#         print(space,"*")
#     elif a==number :
#         print(space,"*" * (number*2-1))
#     else:
#         print(space,"*"," " *(a*2-4),"*")
         
'''
Butterfly Pattern:
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

'''
# number = int(input("Enter Number : "))
# for i in range (1,number+1):
#     first= '* ' * i
#     second='* ' * i
#     space="    " * (number-i-1)
#     if i < number :
#          print(first,space,second)
#     else :
#         print("* "*(number*2-1))
# for j in range (1,number):
#     down_first = "* " * (number-j)
#     down_space= "    " * (j-1)
#     down_second = "* " * (number-j)
#     print(down_first,down_space,down_second)

'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *

'''
# number = int(input("Enter number : "))
# for i in range (1,number+1):
#     star="* " * i
#     space=" " * (number-i)
#     if i ==1 :
#       print(space,star)
#     else :
#         print(space,"*","  "*(i-2),"*")
# for j in range(1,number):
#     down_space=" " * j
#     if j == number-1:
#         print(down_space,"*")
#     else :
#         print(down_space,"*","  "*(number-2-j),"*")


#####  output ###### 

# number=int(input("Enter Number : "))
# for i in range (number):
#   for j in range(i,number):
#     print(" ",end=" ")
    
#   for a in range (i):
#     if a == 0 or i==number-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
  
#   for b in range (i+1):
#     if i==number-1 or b == i:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
            

'''
          * 
        *   * 
      *       * 
    *           * 
  * * * * * * * * * 
'''

# number=int(input("emter number: "))

# # this code work for write mani 

# for i in range (number):
  
#   # This part is M
  
#   for j in range (number):
#     if j==0 or j==number-1 or (i==j and i <= number//2) or (i+j==number-1 and i <= number//2):
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
      
#     # this part is A
    
#   for a in range (i,number):
#     if a == number-1:
#       print("*",end=" ") 
#     else:
#       print(" ",end="")
#   for b in range (i):
#     if b==i-1 or i==number//2:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
      
#   # this  part is N
#   for x in range (i,number):
#     print(" ",end="")

#   for c in range (number):
#     if c==0 or c==number-1 or i==c:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
      
#   # This part is I 
  
#   for d in range (number):
#     if i == 0 or i == number-1 or d==number//2:
#       print(" *",end="")
#     else:
#       print(" ",end=" ")
  
#   print()

