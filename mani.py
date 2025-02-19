'''
ROW
first lint ...... i==0
last line ....... i==n-1
 COLUMN
first line...... j==0
las line ....... j == n-1
MEDIAL ROW OR COLUMN
medial row ....... i==n//2
medial column..... j==n//2

major diagonal ...... i==j
lef diagonal...........i+j==n-1
'''
number = int(input("Enter Number : "))

# for i in range (number):
#     for j in range (i+1):
#         print("*",end=" ")
#     print()
    
####  output ######

'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
# for i in range (number):
#     for j in range (i,number):
#         print("*",end=" ")
#     print()
    
####  output ######

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

# for i in range (number):
#     for j in range (i+1):
#         print(" ",end=" ")
#     for q in range(i,number):
#         print("*",end=" ")
#     print()

####  output ######
'''
 * * * * * 
    * * * * 
      * * * 
        * * 
          * 
'''
# for i in range (number):
#     for j in range (i+1):
#         print("*",end=" ")
#     for a in range (i,number):
#         print(" ",end=" ")
#     for b in range (i,number):
#         print(" ",end=" ")
#     for c in range (i+1):
#         print("*",end=" ")
#     print()
# for I in range (number):
#     for J in range (I,number):
#         print("*",end=" ")
#     for A in range (I+1):
#         print(" ",end=" ")
#     for B in range (I+1):
#         print(" ",end=" ")
#     for C in range (I,number):
#         print("*",end=" ")
#     print()

####  output ######

'''
*                     * 
* *                 * *
* * *             * * *
* * * *         * * * *
* * * * *     * * * * *
* * * * *     * * * * *
* * * *         * * * *
* * *             * * *
* *                 * *
*                     *
'''

# for i in range (number):
#     for j in range (i+1):
#         print(" ",end=" ")
#     for a in range(i,number):
#         print("*",end=" ")
#     for b in range (i,number):
#         print("*",end=" ")
#     print()
# print(" " * (number*2),"*")

####  output ######
'''
  * * * * * * * * * * 
    * * * * * * * * 
      * * * * * * 
        * * * * 
          * * 
           *
'''
# print(" " * (number*2),"*")
# for i in range (number):
#     for j in range (i,number):
#         print(" ",end=" ")
#     for a in range (i+1):
#         print("*",end=" ")
#     for b in range (i+1):
#         print("*",end=" ")
#     print()
    
#####  output ######

'''
           *
          * * 
        * * * * 
      * * * * * * 
    * * * * * * * * 
  * * * * * * * * * *
'''
# print(" "*(number*2),"*")
# for i in range (number):
#     for j in range (i,number):
#         print(" ",end=" ")
#     for a in range (i+1):
#         print("*",end=" ")
#     for c in range (i+1):
#         print("*",end=" ")
#     print()
# for I in range (1,number):
#     for J in range (I+1):
#         print(" ",end=" ")
#     for A in range (I,number):
#         print("*",end=" ")
#     for B in range (I,number):
#         print("*",end=" ")
#     print()
# print(" " * (2*number),"*")

#####  output ######

'''
           *
          * * 
        * * * * 
      * * * * * * 
    * * * * * * * * 
  * * * * * * * * * * 
    * * * * * * * * 
      * * * * * * 
        * * * * 
          * *
           *
'''
# for i in range (number):
#     for j in range (i,number):
#         print(" ",end="")
#     for a in range (i+1):
#         print("*",end=" ")
#     print()
# for I in range (1,number):
#     for J in range (I+1):
#         print(" ",end="")
#     for A in range (I,number):
#         print("*",end=" ")
#     print()
    
#####  output ######

'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''
# for i in range (number):
#     for j in range (number):
#         if i==0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#####  output ######

'''
* * * * * 




'''
# for i in range (number):
#     for j in range (number):
#         if i==number-1:
#             print("*",end=" ")
#         else :
#             print(" ",end=" ")
#     print()

#####  output ######

'''




* * * * *
'''
# for i in range (number):
#     for j in range (number):
#         if i == 0 or i == number-1:
#             print("*",end=" ")
#         else :
#             print(" ",end=" ")
#     print()

#####  output ######   
'''
* * * * * 



* * * * * 
'''

# for i in range (number):
#     for j in range (number):
#         if j ==0 :
#             print("*",end=" ")
#         else : 
#             print(" ",end=" ")
#     print()

#####  output ######   

'''
*
*
*
*
*
'''
# for i in range (number):
#     for j in range (number):
#         if j == number-1:
#             print("*",end=" ")
#         else :
#             print(" ",end=" ")
#     print()

#####  output ###### 

'''
        * 
        * 
        * 
        * 
        * 
'''

# for i in range (number):
#     for j in range (number):
#         if j==0 or j==number-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#####  output ###### 

'''
*       * 
*       * 
*       * 
*       * 
*       * 
'''
# for i in range (number):
#     for j in range (number):
#         if i==0 or j==0 or i==number-1 or j == number-1:
#             print("*",end=" ")
#         else:
#              print(" ",end=" ")
#     print()

#####  output ###### 

'''
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''
# for i in range (number):
#     for j in range (number):
#         if i == number//2:
#             print("*",end=" ")
#         else :
#             print(" ",end=" ")
#     print()
    
#####  output ###### 
'''


* * * * * 


'''
# for i in range (number):
#     for j in range (number):
#         if j == number//2:
#             print("*",end=" ")
#         else : 
#             print(" ",end=" ")
#     print()

#####  output ###### 

'''
    *     
    *     
    *     
    *     
    * 
'''
# for i in range (number):
#     for j in range (number):
#         if i == number//2 or j == number//2 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
        
#####  output ###### 

'''
    *     
    *     
* * * * * 
    *     
    *   
'''
# for i in range (number):
#     for j in range(number):
#         if i==0 or j==0 or i==number-1 or j == number-1 or i==number//2 or j==number//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#####  output ###### 

'''
* * * * * 
*   *   * 
* * * * * 
*   *   * 
* * * * * 
'''
# for i in range (number):
#     for j in range (number):
#         if i+j==number-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#####  output ###### 

'''
        * 
      *   
    *     
  *       
*
'''
# for i in range (number):
#     for j in range(number):
#         if i==j :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#####  output ###### 

'''
*
  *       
    *     
      *   
        * 
'''
# for i in range (number):
#     for j in range (number):
#         if i==j or i+j==number-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#####  output ###### 

'''
*       * 
  *   *   
    *     
  *   *   
*       * 
'''
# for i in range (number):
#     for j in range (number):
#         if i==0 or j ==0 or i==number-1 or j == number-1 or i+j==number-1 or i==j :
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(number):
#     for j in range (number):
#         print("*",end=" ")
#     print()
#####  output ###### 

'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
# for i in range (number):
#   for j in range (i+1):
#     if j==0 or j==i or i==number-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
#####  output ###### 

'''
* 
* * 
*   * 
*     * 
* * * * * 
'''
# for i in  range (number):
#   for j in range (i,number):
#     if i==j  or j==number-1 or i == 0:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

#####  output ###### 

'''
* * * * * 
*     *
*   *
* *
*
'''

# for i in range (number):
#   for j in range (i,number):
#     print(" ",end=" ")
    
#   for a in range (i):
#     if i == number-1 or a==0:
#        print("*",end=" ")
#     else:
#       print(" ",end=" ")
       
#   for b in range (i+1):
#     if i == number-1 or b == i :        
#       print("*",end=" ")               
#     else :                              
#       print(" ",end=" ")    
                  
#   print()

for i in range (number):
  for j in range (i,number):
    print(" ",end=" ")
  for a in range (i):
    if i == number-1 or a==0:
       print("*",end=" ")
    else:
      print(" ",end=" ")
       
  for b in range (i+1):
    if i == number-1 or b == i :        
      print("*",end=" ")               
    else :                              
      print(" ",end=" ")                
  print()

#####  output ###### 

'''
          * 
        *   * 
      *       * 
    *           * 
  * * * * * * * * * 
'''
# for i in range(number):
#   for j in range (i+1):
#     print(" ",end=" ")
  
#   for a in range(i,number-1):
#     if a==i :
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   for b in range (i,number):
#     if b == number-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
#####  output ###### 


'''
  *                   *   
    *               *   
      *           *   
        *       *   
          *   *   
            *
'''
# # upper part
# for i in range (number):
#   for j in range(i,number):
#     print(" ",end=" ")
    
#   for a in range(i):
#     if a == 0 :
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
  
#   for b in range (i+1):
#     if b == i :
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
# #dow part
# for I in range (number):
#   for J in range (I+1):
#     print(" ",end=" ")
  
#   for A in range (I,number-1):
#       if A == I:
#         print("*",end=" ")
#       else:
#         print(" ",end=" ")
#   for B in range(I,number):
#     if B==number-1 :
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
#####  output ###### 

'''
          *
        *   *
      *       *
    *           *
  *               *
  *               *
    *           *
      *       *
        *   *
          *
'''
# for i in range (number):
#   for j in range (i,number):
#     print(" ",end="")
#   for a in range (i+1):
#     if a==0 or i==number-1 or a== i:
#        print("*",end=" ")
#     else:
#       print(" ",end=" ")
  
#   print()

#####  output ###### 

'''
     * 
    * * 
   *   * 
  *     * 
 * * * * * 
'''
# for i in range (number):
#   for j in range (i,number):
#     print(" ",end="")
  
#   for a in range (i+1):
#     if a==0 or i==number-1:
#       print("*",end="")
#     else:
#       print(" ",end="")
      
#   for b in range (i):
#     if b == i-1 or i == number-1:
#       print("*",end="")
#     else:
#       print(" ",end="")  
#   print()

# for I in range (number-1):
#   for J in range(number):
#       if J==number//2:
#         print(" *",end=" ")
#       else:
#         print(" ",end=" ")
#   print()
#####  output ###### 
"""
     *
    * *
   *   *
  *     *
 *********
     *     
     *     
     *     
     *  
"""
# for i in range (number):
#   for j in range (i,number):
#     print(" ",end="")
  
#   for a in range (i+1):
#     if a==0 or i == number-1:
#       print("*",end="")
#     else:
#       print(" ",end="")
#   for b in range (i):
#     if b==i-1 or i == number-1:
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

# for i in range (number):
#   for j in range (number):
#     if j==0 or i==number-1 or j==number-1:
#       print(" *",end="")
#     else:
#       print(" ",end=" ")
#   print()
#####  output ###### 
"""
     *
    * *
   *   *
  *     *
 *********
 *       *
 *       *
 *       *
 *       *
 * * * * *
"""
# for i in range (number):
#   for j in range (i+1):
#     print(" ",end="")
#   for a in range (i,number):
#     print("*",end=" ")
#   print()

# for I in range (1,number):
#   for J in range (I,number):
#     print(" ",end="")
#   for A in range (I+1):
#     print("*",end=" ")
#   print()

#####  output ###### 
"""
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
"""
# this code perfectly work for even or odd numbers input
# upper part

# for i in range (number):
#   for j in range (i+1):
#     print(" ",end='')
#   for a in range (i,number):
#     if i == 0 or a==i or a==number-1:
#        print("*",end=" ")
#     else :
#       print(" ",end=" ")
#   print()
  
  #lowe part
  
# for I in range (1,number):
#   for J in range (I,number):
#     print(" ",end="")
#   for A in range (I+1):
#     if I == number-1  or A==0 or A == I:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

      #or 
  # this code perfectly work for only odd numbers
  
# for i in range (number):
#   for j in range (number):
#     if i == j or j+i == number-1 or i == 0 or i== number-1:
#       print("*",end=" ")
#     else : 
#       print(" ",end=" ")
#   print()
#####  output ###### 
"""
 * * * * * 
  *     * 
   *   * 
    * * 
     * 
    * * 
   *   * 
  *     * 
 * * * * * 
"""

#####  output ###### 
"""

"""

'''

#####  output ###### 

'''
'''

#####  output ###### 

'''

            
