## Day - 1 
'''
List a collection of elements with various types.It is mutable mean
we can change the values after creation of list also. it allow duplicates and allow indexing List with [] brackets..
'''
###########   CREATION   ##############

# L1=[]
# L2 = ["Mani,kolla","kolla",1,2,5,2.5,0.123]
# L3 = list([1,"Ram"])
# print(type(L1))
# print(type(L2))
# print(type(L3))
# print(L1)
# print(L2)
# print(L3)

#Creation of list Dynamically by using eval() function.

# L1 = eval(input("Enter the L1 Elementnt : "))
# ## Take input use Complesary [] use brackets []
# print(type(L1))
# print(L1)

##Creation of list by using range() function.

# l1 = list(range(1,11))
# print(l1)

#List can hold any complex data type like dict,tuple, etc

# L1=[40,{"name":"Ram"},list((10,20,30))]
# print(type(L1))
# print(L1)

##################### 2. Access ############################

# list = [1,2,3,4,5,6,7]
# print(list[0])
# print(list[2])
# print(list[-5])
# print(list[-1])
# print(list[6])


# list = [1,2,3,4,5,6,7]

# print(list[:0])
# print(list[2:])
# print(list[:-5])
# print(list[-1:])
# print(list[6:])

# print(list[::3])

########### Iterating the list#################

#Visiting all the elements in a sequence is called Traversing

# list = ["John", "David", "James", "Jonathan"]
# i = 0
# for i in list :
#     print(i)
# while i < len(list):
#     print(list[i])
#     i+=1
    
# Visiting the elements in a sequence and print the particular index

# list=[30,40,50,"Ram",1,"Gopal",80]

# for i in range (len(list)):
#     if i == 2 :
#         print(list[i])
# i=0
# while i < len(list):
#     if i == 5 :
#         print(list[i])
#         break
#     i+=1
    

###WAP to display list elements of a list along with positive and negative index.###


# list=[10,20,30]
# n=len(list)

# for i in range(n):
#     print(f"{list[i]}is present at index {i}/{i-n}")
    
    
# list2 = [10,20,30]
# N = len(list2)
# z=0

# for i in list2 :
#     print(f"{i} is present index {z} / {z-N}")
#     z+=1

# i = 0
# n = len(list2)
# while i < n :
#     print(f"{list2[i]} is present index is {i} / {i-n}")
#     i+=1
    
    
#########3. updating the list Elements###############

# L1=[1,2,3,4,10,20,30]
# L1[1]=30
# L1[2:3]=30,40    # already exsited values are removed and enter new values 
# print(L1)

#Update the list by using Iter method

# L1=[1,2,3,4,10,20,30]
# l=len(L1)
# for i in range (2,5):
#     element =int(input("Enter Element : "))
#     L1.insert(i,element)
# print(L1)


    
################### Using methods on list ######################

####Append Method(Add at end)##Drawback we cannot add at Specified location-

# l1=[1,2,4,5,6,8,1]
# l1.append(40)
# print(l1)

# number_of_elements = int(input("Enter NUmber of elements your choise : "))

# for i in range (number_of_elements):
#     add_elements = int(input(f"Enter emelents {i}: "))
#     l1.append(add_elements)
# print(l1)

###Create a list by adding use range funcation 

# l1=[]
# for i in range (20):
#     l1.append(i)
# print(l1)


#####Insert Method(Insert the element at specified location)


# l1=[1,2,3,4,2,5,6,7,2,8,9,10]
# l1.insert(20,50)##insert at end because there are no such indexes
# l1.insert(-30,25)#insert at start because there are no such indexes
# print(l1)


#Update the list by using insert & Iter method

# L1=[1,2,3,4,10,20,30]
# start = int(input("Enter Start index :"))
# end = int(input("Enter end index :"))
# for i in range (start,end):
#     add_element = int(input(f"Enter {i}element"))
#     L1.insert(i,add_element)
# print(L1)

#######Count Method(Used to count how many times the element is present)

# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# print(List.count(1))

#####If we want to count multiple values then we go for iter

# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# count=0
# element=int(input("Enter requride element : "))
# for i in List :
#     if i == element :
#         count+=1
# print(count)

######Index Method(Used to know the index number of specific element multiple times )

# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# print(List.index(2))

# count=0
# element = int(input("Enter Element : "))
# for i in List :
#     if i == element :
#         count+=1
#         print(List.index(i))
#     if count == 1 :
#         break

#######pop Method used to delete element by index by default last element if we not mention index

# List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
# List.pop() #By default last element
# print(List)
# List.pop(3)  #By index number
# print(List)

# start= int(input("Enter requoired index value ; "))
# end = int(input("Enter requied index value+1 : "))
# for i in range (start,end):
#     print(List.pop(i))
# print(List)

# element=int(input("Enter number :" ))
# for i in range(len(List)):
#     if i == element:
#         List.pop(element)
#         print(List)
    

#######extend method (Used to extend the list or add a sublist)

# list1=[1,2,3,4]
# list1.extend([4]) #we cannot process this extend as sublist
# print(list1)

# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l1.extend(l2)# Add List2 to List1
# print(l1)

#creation of a list by using split()

# a= "welcome to python world"
# print(type(a))
# print(a.split())

# a = "wel-come to py-tho wo-rld"
# print(a.split('-'))

######Sum Method  ##############

# l1=[1,2,3,4,5,6,7]
# print(sum(l1))
# l2=[]
# for i in range (1,5): # sum perticular index 
#    l2.append(l1[i])
# print(l2)
# print(sum(l2))


######Length Method #########


# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# element=int(input("Enter element  : "))
# print(len(List))
# for i in range (len(List)):
#     if List[i]== element :
#         print(i)
        
        
 ###### Min method #######
 
# list = [8, 2, 3, 5,8,9]   
# print(max(list)) 
   
# for i in range (len(list)):
#     for j in range (i+1,(len(list))):
#         if list[i] > list[j]:
#             list[i],list[j]=list[j],list[i]
# print(list)

#########Copy Method ########


# List = [8, 2, 3, 5,8,9]
# print(List)
# m=List.copy()
# print(m)
# List.append(10)
# print(List)


###### Clear the complete list #########

# List = [8, 2, 3, 5,8,9]
# List.clear()
# print(List)


####del Method used to delete specific element by index

# List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

# del List[0]
# print(List)

# List1 = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

# Index=int(input("Enter index number : "))
# for i in range (len(List1)):
#     if i == Index:
#         del List1[Index]
        
#         print(List1)

#######Remove method(Used to Delete the specified element and by specific index element)

# l1=[1,2,3,4,5,6,7,8,9,10,2]
## remove through element

# l1.remove(2) # remove first element in list not all repeated elments 
# print(l1)

## Remove thorough index value 

# l1.remove(l1[2])
# print(l1)

# l1=[1,2,2,3,4,5,6,7,8,9,10,2]
# print(len(l1))

# choice=int(input("Enter your Choice elment : "))

# for i in range (len(l1)-1):
    
#     if l1[i] == choice :
#         l1.remove(l1[i])
# print(l1)

# # for i in l1 :
#     if i == choice:
#         l1.remove(choice)
# print(l1)
    
# list = [0,1,2,3,4]
# print("printing original list: ")
# for i in list:
#     print(i,end=" ")

# list.remove(2)
# print("\nprinting the list after the removal of second element...") 

# for i in list:
#     print(i,end=" ")


##### reverse method It is used to reverse the list.

# List = [8, 2, 3, 5,8,9]
# List.reverse()
# print(List)

######sort() It is used to sort the order.

# List = [8, 2, 3, 5,8,9]
# List.sort() 
# print(List)
# List.sort(reverse=True)
# print(List)

#####Concatination of list#########

# L1=[20,30,40,50,60]
# S1=['Ram','Priyanka',40,50]
# C1=L1+S1
# print(C1)

#Repetition of Lists

# L1=[10,20,40]
# Rep=L1*5
# print(Rep)

#WAP to check the number is present in the list or not until it matches

# L1=[10,20,30,40,50,60]
# choice=int(input("ENter your lucky number : "))

# while True :
#     if choice in L1 :
#         print(f"Yes your number is present \n{choice} index is {L1.index(choice)}")
#         break
#     else:
#         print("The number is not present")
#         choice=int(input("ENter your lucky number : "))

#WAP to print the list of elements in reverse order  

# list=[10,20,40,50,60]
# n=len(list)-1
# while n >=0 :
#     print(list[n])
#     n-=1
# list.sort(reverse=True)
# print(list)

#WAP to print the elements in  sort order by using for or while

list=[10,50,30,40,20]

# for i in range (len(list)):
#     for j in range (i+1,len(list)):
#         if list[i] > list[j]:
#             list[i],list[j]=list[j],list[i]
# print(list)

# n=0
# while n <= len(list)-1:
#     m=0
#     while m+1 <len(list):
#         if list[n] < list[m]:
#             list[n],list[m]=list[m],list[n]
#         m+=1
#     n+=1
# print(list)

 #WAP to print min and max values in the list
 
# list=[10,30,4,50,35,60]
# min=list[0]
 
# for i in list:
#     if i < min :
#         min=i
# print(min)

'''wap to search a value from a list then display its index, if the value is present
multiple times then print its all indices and also count the number of times that value 
is repeated in the list.'''

# list=[10,20,30,40,50,10,20,30,40]
# search=int(input("Enter the value of you want to search :"))
# i=0
# count=0
# while i < len(list):
#     if search == list[i]:
#         count+=1
#     i+=1
# print(f"{search} is present {count} times")

# count1=0
# for i in list:
#     if search==i:
#         count1+=1
# print(f"{search} is present {count1} times")

# l1={"Hi ", "Hello "}
# l2={"Ram", "Banti","Seetha"}
# new_list=[]
# for i in l1:
#     for j in l2:
#         new_list.append(i+j)
# print(new_list)

# l1={"Ram", "Banti","Seetha"}
# new_list=[]
# for i in l1:
#     new_list.append(i[0]+i[-1])
# print(new_list)

'''
#enumerate function used to print the value and index
#By using enumerate the code will decrease.
'''

# l1=[10,20,30,40,50]

# for i in enumerate(l1):
#     print(i)

#If list is present inside another list is called as Nested List.
## 0  1   2  3  4[1,2,3]  5   6

l=[10,20,30,40,[41,42,43],50,60]

###Negative index as well

# print(l[2])
# print(l[4][1])


#Nested List in a Matrix
# l=[[10,20,30],[40,50,60],[70,80,90]]

# print(l)

# ####print row wise matrix

# print(l[0])
# print(l[1])
# print(l[2])

# l=[[10,20,30],[40,50,60],[70,80,90]]
# for i in l :
#     print(i)


#If you want to create a list from iterable objects like list,tuple,range,dict etc
#By writing very less code in efficient way then we can go for list comprehensions.

####   Normal example  #####

# list=[]
# for i in range (11):
#     list.append(i)
# print(list)

####   By using list comprehension  ######

'''l1=[i for i in range (11)]
print(l1)

l1 = [i*i for i in range (11)]
print(l1)

l1=[i*2 for i in range (11)]
print(l1)

l1 = [i for i in range(2,21) if i % 2 ==0]
print(l1)
'''
#Create a list by add the elements which is containing letter a
'''names=["rama","banti","roji"]
l1=[i for i in names if "a" in i]
print(l1)
'''
#Replace the list element
# names=["rama","banti","roji"]
# l=[i if i !="banti" else 'hello' for i in names]
# print(l)

