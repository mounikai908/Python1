number=int(input("emter number: "))

# this code work for write mani 

for i in range (number):
  
  # This part is M
  
  for j in range (number):
    if j==0 or j==number-1 or (i==j and i <= number//2) or (i+j==number-1 and i <= number//2):
      print("*",end=" ")
    else:
      print(" ",end=" ")
      
    # this part is A
    
  for a in range (i,number):
    if a == number-1:
      print("*",end=" ") 
    else:
      print(" ",end="")
  for b in range (i):
    if b==i-1 or i==number//2:
      print("*",end=" ")
    else:
      print(" ",end=" ")
      
  # this  part is N
  for x in range (i,number):
    print(" ",end="")

  for c in range (number):
    if c==0 or c==number-1 or i==c:
      print("*",end=" ")
    else:
      print(" ",end=" ")
      
  # This part is I 
  
  for d in range (number):
    if i == 0 or i == number-1 or d==number//2:
      print(" *",end="")
    else:
      print(" ",end=" ")
  
  print()

