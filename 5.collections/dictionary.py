'''
By using list,set,tuple we can store only values
Some times as a programmer we require to key values as a 
pair in that case we can go to dictionary
'''

########Creating Dictionary########

# my_dict={}
# my_dict=dict()
# print(my_dict)
# print(type(my_dict))

'''# adding a key value to empty dict'''

# my_dict={}
# my_dict["name"]="mani"
# print(my_dict)

'''# dictionary with integer keys '''

# my_ditc={1:"apple",2:"ball"}
# print(my_ditc)
# print(my_ditc[1])

'''# dictionary with mixed keys'''

# my_dict={"name" : "mani",1:[2,5,3,5]}
# print(my_dict)
# print(my_dict["name"])

'''# using dict()'''

# my_dict=dict({1:"apple",2:"ball"})
# print(my_dict)

'''# from sequence having each item as a pair '''

# my_dict=dict([(1,"apple"),(2,"Raju"),("name","ravi")])
# print(my_dict)

# my_dict=dict(((1,"apple"),(2,"mani"),("name","kolla")))
# print(my_dict)

# my_dict=dict({(1,"apple"),(2,"mani")})
# print(my_dict)

'''#####Create the dictionary dynamically'''

# dict={}
# while True:
#     key=input("enter Key : ")
#     value=input("Enter value : ")
#     dict[key]=value
    
#     choice =input("Enter the choice you want to add more elements in to dictionary [Y/N] : ")
    
#     if choice == "N" :
#         break
# print(dict)

############ Accessing the elements in the dict #############

# my_dict={"name" : "mani","age" : 25}
# print(my_dict["age"])

'''#We can try to access the key that not exist'''

# my_dict={"name" : "mani","age" : 25}
# print(my_dict["address"])  # key error

'''###Check whether key is existed or not#########'''

# my_dict = {"name":"mani","age":30}
# print("age" in my_dict)

'''##### Access the elements by using for loop'''

# my_dict={1:"mani",2:"kolla"}

# for i in my_dict:
#     print(i ,my_dict[i]) #keys= i and values=dict[i]'''

'''#######Modification'''

# my_dict={1:"mani",2:"kolla"}

# my_dict[1]="krishna" ##Here we modify the values with the help of key not index number
# print(my_dict)

# my_dict[3]="raju" #We are adding elements to the dictionary
# print(my_dict)

'''#########Delete a key value from dictionary'''

# my_dict={1:"mani", 2:"krishna"}

# del my_dict[1] #Here we deleted with the help of key not index
# print(my_dict)

'''#############Methods###########'''

''' Get method 
It is use to give the value corresponding to that key. If key is not present it returns No
'''
# d={1:"mani",2:"kolla"}
# print(d.get(1))
# print(d.get(3))
# print(d.get(3 ," Please check the key is present or not" ))

'''#items method
item return the complete items in the dictiionary both key and values
'''
# d={1:"ram",2:"Seetha"}
# print(d.items())

'''Keys method'''

# for i in d.items():
#     print(i)
    
''' It returns the keys only'''

# d={1:"ram",2:"Seetha"}
# print(d.keys())

# for i in d.keys():
#     print(i)

'''#pop method#
It is used to remove the key and value. If the key is not present then it will raise KeyError.
'''

# d={1:"ram",2:"Seetha"}
# d.pop(1)  #Here we have to pass atleast one key. If no key is passed it raise error.
# print(d)



'''
#pop Item Method
# It is used to remove the last inserted item in dict
# '''

# d={1:"ram",2:"Seetha"}
# d.popitem()
# print(d)


'''
Set Default method
Here an argument we will provide key and value. It is used to return the value with that key. 
If the key is not present then the value will be added as new item to dictionary.'''

d={1:"ram",2:"Seetha"}
# print(d.setdefault(11, "Rama Krishna"))
# print(d)

# print(d.setdefault(2, "Harini"))
# print(d)



'''
#Update Method
It is used to add all the elements from one dict to another dict.'''

# d1={1:"ram",2:"Seetha"}
# d2={3:"Raju",4:"Harini"}
# d1.update(d2)
# print(d1)

'''#If the key is present in both dict then it will be consider the updated one'''

# d1={1:"ram",2:"Seetha"}
# d2={2:"Raju",4:"Harini"}
# d1.update(d2)
# print(d1)

'''#copy Method
#It is used to copy(Shallow Copy) all the item from one dict to another dict.'''

# d1={1:"Ram",2:"Krishna"}
# d2=d1.copy()

# print(d1)
# print(d2)
# print(id(d1))   #112233
# print(id(d2))   #112234

'''
#Both dict are pointing to different memory locations so if we will made 
# any changes on any particular dictionary it will not reflect to another dict.

'''

# d1={1:"Ram",2:"Krishna"}
# d2=d1   #assign
# print(d1)
# print(d2)
# print(id(d1))  #112233
# print(id(d2))  #112233

'''
#clear Method
#It is used to remove all the items of a dict but then our dict will become empty.
'''
# d1={1:"Ram",2:"Krishna"}
# print(d1)
# d1.clear()
# print(d1)


'''
#fromkeys Method
#It is used to create a new dict from given iterable(list, tuple, range etc) and value(it is optional)
'''
# l=[10,20,30]
# d=dict.fromkeys(l)
# print(d)

# t=(10,20,30)
# d=dict.fromkeys(t)
# print(d)

# r=range(5)
# d=dict.fromkeys(r)
# print(d)

# r=range(3)
# d=dict.fromkeys(r,"hello")
# print(d)

'''
#Count the No of occurance present inside the string.

'''
# s="manikolla"
# d={}
# for i in s :
#     d[i]=d.get(i,0)+1
# print(d)

# for i,j in d.items():
#     print(f"{i} is present {j} times")

# name="mani kolla is the best student"
# d={}
# for i in name:
#     if i!=" ":
#          d[i]=d.get(i,0)+1
# for a,b in d.items():
#     print(f"{a} is present {b} times")

#Add the elements in to dictionary in run time

d={}
# while True:
#     name=input("Enter your name:")
#     place=input("Enter your place:")
#     d[name]=place
#     choice=input("Do you want to add more candidates [Y/N]:")
#     if choice=="N":
#         break
# print(d)


'''#Access the elements from dictionary at run time
'''

# while True:
#     name=input("Enter the name :")
#     place=d.get(name)
#     print(f"Hi {name} you are from {place}")
    
#     choice=input("Do you want to search more[Y/N]:")
    
#     if choice=="N":
#         break

#Dictionary Comprehensions

# d={i:i for i in range(0,5)}
# print(d)
# print(type(d))

# d={i:i*i for i in range(0,5)}
# print(d)
# print(type(d))

# l=[10,20,30,40]
# d={i:3*i for i in l}
# print(d)

# name=["Rama", "Krishna","Gopal"]
# d={i:len(i) for i in name}
# print(d)

#Nested Dictionary
students={
1:{"name":"Rama Krishna","place":"Kakinada"},
2:{"name":"Rajaram","place":"rajahmundry"}
}

# for i,j in students.items():
#     print("student id is : ",i)
    
#     for k in j:
#         print(f"{k} is: {j[k]}")
#     print('-'*20)


# #Merging Dict Elements

# d1={"Name":"Rama"}
# d2={"Place":"Kakinada"}

# d3={**d1, **d2}
# print(d3)
    
    