number=int(input("enter number : "))
name=input("Enter your name enter captial latters only : ")


for latter in name:
    for i in range(number):
    # This code print A letter
        if latter == "A":
        
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
                    
            print()

        # This code print B letter
        elif latter == "B":
        
            for b in range (number):
                if b == 0 or b==number-1:
                    print("*",end=" ")
                elif i==0 or i==number-1 :
                    if b < number-2:
                        print("*",end=" ")
                elif i==number//2:
                    if b== number-2:
                        continue
                    else:
                         print("*",end=" ") 
                else:
                    print(" ",end=" ")
            print()

        # This code print C letter
        elif latter == "C":
       
            for c in range (number):
                if (i==0 or i == number-1):
                    if c == 0 :
                        print(" ",end=" ")
                    else:
                        print("*",end=" ")
                elif c==0:
                    if i > 0 and i < number-1:
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
            print() 
            
        elif latter == "D":
        # This code print D letter

        
            for d in range (number):
                if i == 0 or i==number-1:
                    if d < number-1:
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
                elif  d == 0 or d == number-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        # This code print E letter
        elif latter == "E":
        
            for e in range (number):
                if i==0 or i == number-1 or e==0 or i == number//2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ") 
            print()
            
        # This code print F letter
        elif latter == "F":   
      
            for f in range (number):
                if i == 0 or i == number//2 or f==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        # This code print G letter
        elif latter == "G":
        
            for g in range (number):
                if i ==0 or i == number-1 or (i==number//2 and g > number//2 -1):
                    if g!=0 :
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
                elif g==0 or (g == number-1 and i > number//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    
        elif latter == "H":        
        # This code print H letter

            for h in range (number):
                if h == 0 or i == number//2 or h == number-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        elif latter == "I":
        # This code print I letter
        
            for I in range (number):
                if i ==0 or i == number-1 or I == number//2 :
                    print("*",end=" ")
                else :
                    print(" ",end=" ")
            print()
        elif latter == "I":
        # This code print J letter

            for j in range (number):
                if i == 0 or j == number//2 or (j ==0 and i > number//2) or (i==number-1 and j < number//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        elif latter == "K":
        # This code print K letter  j == 0 or i + j == height // 2 or i - j == height // 2

        
            for k in range (number):
                if  k==0 or i+k==number//2+1 or i-k == number//2-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ") 
            print()
         
'''elif latter == "L":
        # This code print L letter

        for i in range (number):
            for l in range (number):
                if l ==0 or i == number-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif latter == "M":
        # This code print M letter

        for i in range (number):
            for m in range (number):
                if m==0 or m==number-1 or (i==m and i<=number//2) or (i+m ==number-1 and i < number//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif latter == "N":
        # This code print N letter

        for i in range (number):
            for n in range (number):
                if n==0 or n==number-1 or i==n :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print() 
    elif latter == "O":
        # This code print O letter

        for i in range(number):
            for o in range (number):
                if i==0  or i == number-1 :
                    if o==0 or o==number-1 :
                        print(" ",end=" ")
                    else:
                        print("*",end=" ")
                elif o==0 or o==number-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif latter == "P":
        #  This code print P letter

        for i in range (number):
            for p in range (number):
                if ((i==0 or i == number//2)and p < number-1) or p==0 or (p==number-1 and (i < number//2)and i > 0):
                    
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif latter == "Q":           
        #  This code print Q letter

        for i in range(number):
            for Q in range (number):
                if i==0  or i == number-1 :
                    if Q==0 or Q==number-1 :
                        print(" ",end=" ")
                    else:
                        print("*",end=" ")
                elif Q==0 or Q==number-1:
                    print("*",end=" ")
                elif i >= number//2 and i-Q == number//2-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        for I in range (number):
            if I == number-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    elif latter == "R":
        #  This code print R letter

        for i in range (number):
            for R in range (number):
                if ((i==0 or i == number//2)and R < number-1) or R==0 or (R==number-1 and (i < number//2)and i > 0) or i-R == number//2-1:
                    
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif latter == "S":          
        #  This code print S letter

        for i in range (number):
            for j in range (number):
                if i==0 or (i==number//2) or (j==0 and (i <= number//2)) or(j==number-1 and i > number//2) or i==number-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                
            print()
    elif latter == "T":
        # This code print T latter 
        for i in range (number):
            for t in range(number):
                if i == 0 or t == number//2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    elif latter == "U":
        #  This code print U letter

        for i in range (number):
            for u in range (number):
                if ((u== 0 or u == number-1) and i< number-1 ) or i==number-1 and (u>0 and u < number-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    elif latter == "V":
        #  This code print V letter

        for i in range (number):
            for v in range (i+1):
                if v ==i:
                    print("*",end=" ")
                else:
                    print("",end=" ")
            for V in range (i,number-1):
                if V == number-2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    elif latter == "W":
        #  This code print W letter

        for i in range ( number):
            for w in range (number):
                if w==0 or w==number-1 or (i==w and i >= number//2) or (w+i==number-1 and i> number//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    elif latter == "X":
        #  This code print X letter

        for i in range (number):
            for x in range (number):
                if i==x or i+x==number-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    elif latter == "Y":
        #  This code print Y letter

        for i in range (number):
            for y in range (number):
                if (y==i and i < number//2)or y+i == number-1  :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    elif latter == "Z":
        #  This code print Z letter

        for i in range (number):
            for z in range (number):
                if i+z==number-1 or i ==0 or i == number-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()'''