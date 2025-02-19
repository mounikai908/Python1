###### Types of Arguments #######
'''
There may be several types of arguments which can be passed at the time of funcation calling .
Default arguments
Keyword argument
Required or positional atguments
Variable- length arguments
'''
# ##Positional Arguments   ########
'''
Required argument are the arguments passed to a funcation in correct positional order.
Here ,the number of arguments in the funcation call should match exactly with the funcation definition.
'''
# # Example 
# def sample(a,b,c):
#     return a,b,c
# print(sample(10,20)) # error because there are no sufficient requried arguments on calling

# # Example 
# def sample(a,b):
#     return "Name is : ",a , " My age is : ",b
# print(sample(30, "Rama Krishna")) # Ther are not in correct position

#### Keyword rguments #####
'''
Python allows us to call the funcation with the keyword arguents. 
This kind of funcation call will enable us to pass the arguments in the random order.
'''
# Example

# def mani(name,age,dep):
#     print("Name : ",name)
#     print("age : ",age)
#     print("Department : ",dep)
# mani("mani",age=25,dep=120)

# Exaample 

# def mani(name1,message,name2):
#     print("Printing the message with ",name1,",",message,"and",name2)
# mani("john",message="hello","david") # error positional argument follows keyword argument


##### Positional argumnet cannot appear after keyword arguments

#### Default arguments ######

'''
While defining a function we can intialize some of the arguments using default values . 
Passing default va;ue to parameter is optional
If we pass value to default argument, existing value will be replaced.
'''

# Example 

# def sample(name,age=25): # Here age is default argument
#     print(name,age)
# sample(name="mani")

# def sample(name,age=25): # Here age is default argument
#     print(name,age)
# sample(name="mani")
# sample(age=30,name="mani kolla")
# sample(20,"kolla mani")

###### Variable - Length Arguments : 
'''
In th elarge project, sometimes we may not know the number of arguments to be passed in advance.
In such cass, Python provides us the flexibility to provide the comma seperated values which are internally
treated as tuples,at the funcation call.

However ,at the funcation definition,we have to define * variable-name
 . Non-Keyword Arguments(*args)
 . Keyworded arguments (**kwargs)
'''
# Example 

# def variablearges(a):
#     print(a)
# variablearges(10)

# def variablearges(a):
#     print(a) # it give an error because we declare one paraametr but we passes two values 
# variablearges(10,20)

# def variablearges(*a):
#     print(a)
# variablearges(10,20,30.35,"Mani") # It will execute because we take it is a pointer like tuple.
# variablearges(name="mani",age=25) # It gives an error because it is in dictinary format.

# def variableargs(*a):
#     print("Elemnets are : ")
#     for z in a :
#         print(z)
# variableargs(10,20,30,40,50,60)

# def variableargs(*names):
#     print("Type of passed argument is : " , type(names))
#     print("Printing the passed arguments....")
    
#     for name in names:
#         print(name)
# variableargs("mani","kolla","hello","that is ")
'''Output:
type of passed argument is  <class 'tuple'>
printing the passed arguments...
mani
kolla
hello
that is '''

# * and ** in funcation call

# def sample(a,b,c):
#     print(a,b,c)
# l=[10,20,30] # this list a one element

# sample(l) # error sample () missing 2 required positional arguments : 'b' and 'c'

# def sample(a,b,c):
#     print(a,b,c)
# s={10,20,30}
# t=(10,20,30)
# l=[10,20,30]
# sample(*s)
# sample(*t)
# sample(*l)

# def sample(**s):
#     print(s)
# d={"a" : 10 , "b" : 20, "c":30}
# sample(**d)