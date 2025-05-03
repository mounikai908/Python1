########  What is comments ##########

'''
Comments are text in written in conde to explain it, which the interpreter 
ignore during the execution. Ther are useful for improving code readibility
and it is help to other easely understand code logic.

Ther are  2 type of comments supports python 

1.Single line comments  also know as in-line comments (indicates # symbol)
2.Multi line comments  also know as block comments (indicute 3 quatations) 

'''

###### What is variable ###########

'''
Variable is the name of address where data will be store in it
        Variable are containers for  stored a variable 

        we can create variable different ways 

                1. We can create one varible to assign one value   a = "mani"
                2.We can create one variable to assing multiple values  a = 10,20,30
                3.We can assing the one value to multiple variables a=b=c=20
                4.We can create multiple variable to assign multiple value in single line (a,b,c=10,20,30)

   Rules of variable creations

        1.Variable name must start with a latters and underscore character 
        2.A variable name cannot start with a number 
        3.A variable name can only contain alpha-Numeric characters and underscore
        4.Variable names are case-sensitive
        5.The reserved words cannot be used naming the variable.
'''

######## What is data ############

'''Raw metarial of requried informatation ex: images, text, etc '''


####### What is globle Variable ###########

'''The variable we created out side of the funcation called global variable 
   global variable  we can access inside the funcation and out side the '''


########### What is data types ##########

'''A data type defines the kind of value a variable can hold in programming.


integr data type  --->  int is denoted with int() 
                        An integer data type represents whole numbers—positive, 
                        negative, or zero—without any fractional or decimal part.
 
float data type   ---> floate numbers we can denoted with float () 
                        A float data type represents numbers with decimal points,
                          allowing for precise calculations.

boolean data type ---> The bool data type represents Boolean values, 
                        which can only be True or False. 
                        It's useful for logical operations and decision-making.
 
complex data type ---> The complex data type represents numbers with both real and imaginary parts. 
                        It's mainly used in mathematical computations and scientific applications

string           ---> A string data type represents sequences of characters, such as letters, numbers,
                         and symbols. It's commonly used for storing text-based data.


list data type   --->  List is a collection of elaments with various data types. 
                        It is mutablle means we caan change the values after creation of list also
                        List with [] 

Tuple data type  ---> A tuple in python similir to list . The difference bitween the two is that we 
                        cannot change the elements of a tuple once it is assigned we can change the elements od a list 
                        Tuple with ()

Set data type    --->  Set is a collection of elements with various datatypes. Set is mutable(we can change)
                        and its elements are immutable(we can't change ). Set  cannot accept duplicate elements.Set cannot folliw Order 
                        Set with {}

dictonary data type---> The dictionary data type in Python is a powerful way to store key-value pairs,
                         allowing fast lookups and structured data storage.

'''

######### What is oprators ###########


'''

An operator in programming is a symbol or keyword that performs 
a specific operation on one or more operands (values or variables).
Operators are essential 

for performing calculations, comparisons, logical decisions, 
and more in code.

1.Arthemitical Operator ---> Arithmetic operators are symbols used in programming and databases 
                             to perform mathematical calculations like addition, subtraction, multiplication, and division.
                             (Arthimetical operators or +,-,*,/,//̣,%)

2.Comparisation Operator ---> A comparison operator is used in programming and databases to compare two values.
                              The result is always a Boolean (True or False).
                              (Comparasition operators are >,<,<=,>=,==,!=) 

3.Logical operator      ---> Logical operators are used in programming and databases to combine multiple conditions
                             and return a Boolean result (True or False). They help make decisions based on multiple comparisons.
                             (Logical operator is (and, or not ))

4.Assignment Operator    ---> An assignment operator is used to assign values to variables in programming.
                              (Assignment operators +=,-=,/=,*=,//=,%=)

5.Bitwisw operator       ---> It looks like you meant "Bitwise operator"—these are used in programming to perform 
                              operations at the binary level, manipulating individual bits of numbers.

6.Membership operator    --->  A membership operator is used in Python to check if a value is present in a sequence, 
                               such as a list, tuple, string, or dictionary.
                                (Membership operator are (in ,not in ))

7.Identify Operator     ---> An identity operator in Python is used to compare the memory address (identity) of two objects, 
                             checking whether they refer to the same object in memory.
                             (Identify Operator are (is ,is not ))

'''

####### What is control statement #########
'''
Control statements are 

1.Conditional statemnt --->  Conditional statements are used in programming to execute a block of code based on 
                             whether a condition is True or False. They help make decisions in a program by controlling the flow of execution
                            (Conditional statements are (if, elif,else ))

2.Loping statemnets    ---> these are used in programming to repeat a block of code multiple times until a condition is met.(Loping statements are (While, For ))
                                A. what is difference bitween while loop and for loop
                                       *  While loop is used when the number of iterations is unknown beforehand
                                       *  For loop is used when the numner of iteretions is know beforehand

3.Transfar Statement   --->  these are used in programming to alter the normal flow of execution 
                             within loops or functions(Transfar statements are (pass,continue,breake))

                             A . What is pass Statement?

                                ---> The pass statement in Python is a placeholder that does nothing when executed. 
                                     It's used in places where a statement is syntactically required but no action is needed
                                     at the moment.

                             B . What is Continue statement ?

                                ---> The continue statement in Python is used inside loops to skip the current iteration 
                                     and move to the next one without breaking the loop.
                        
                             C . What is Break statement ?

                                ---> The break statement in Python is used inside loops to stop execution immediately,
                                     exiting the loop before it completes all iterations.



'''








###### What is funcation #########

'''Funcation is collection statements or a pieace of code to perform to a specific task

        ## Advantages 

                 1. Code Reusability
                 2. Improve Modularity             
'''

##### Types of funcations ##########

'''
1. Buils in funcation

2. User Defined Funcations.

  *** Build in Funcations --> This Funcations are already created by Python people 
        such type of funcation are called as predefin funcations or Build in funcations.

  *** User Defind Funcations --> These Funcations are created by users as per requirements.

  ***Use of funacations***
        If we want to execute a piece of code for multiple times then we go for functions.
'''

##### What is Parameter  ######

'''Parameters is just like variable present inside the function while defining

def add(a,b):  --->  # parameters / Formal arguments
    print(a+b)
    
add(10,20) --->   # arguments / actual arguments
'''


## What is call by vale  ##

'''If we made any chages on called function it will 
not reflect on outside the function when we call with value.'''

## What is call by reference ##

'''If we made any chages on called function it will reflect on outside the function 
when we call with reference.'''


###  NOTE   ####

'''Python does not support Call by value or Call by reference it support by call by object reference.
 When we pass immutable objects like int,float, tuple it acts like call by value (i.e., modify that object and create new object.) 
 and when we pass mutable objects like list, dictionary it acts like call by reference (i.e., modify that object and will not create new object.).'''


## Whaat is return ##

'''In functions internally return a value by default as None

        return statement only be at end of the function. If we give return statement 
in the middle after return statement remaining statement will not going to be executed.'''


### What is the difference Return And Print in a Funcation ?

'''### Return  :-  Sends a value back to the caller and  terminates Funcation Execution

  ### Print  :- Displays output but doesn't return anything

'''

### What are arguments and keywork Arguments and what are difference  ?

''' 
    ### Arguments :- Allows a Funcation to accept any number of positional arguments

    ###  Keywodrd Argument :- Allows a Funcation to accept any number of Keyword Rguments

'''


### What is the difference between a funcation and a method in python ?

''' A Funcation is an independent block of code defined using def 
    A method is a funcation associated with a class / object
'''



### Types of Arguments  ###

'''There may be several types of arguments which can be passed at the time of function calling.
•	Default arguments
•	Keyword arguments
•	Required or positional arguments
•	Variable-length arguments'''

        ### 1. Default arguments###

'''                     While defining a function, we can initialize some of the arguments using default values. Passing default value to parameter is optional.
                        If we pass value to default argument, existing value will be replaced.
                        
                        ### How to handel ###

                                Default arguments assign values automatically if no values is passed by the caller.

                                Default values are set in the funcation definition
                        
                        '''


        ### 2. Keyword Arguments###
'''             Python allows us to call the function with the keyword arguments. 
                This kind of function call will enable us to pass the arguments in the random order.'''


        ### 3. Positional Arguments:
'''             Required arguments are the arguments passed to a function in correct positional order. 
                Here, the number of arguments in the function call should match exactly with the function definition.'''


        ### 4. Variable-Length Arguments ###
'''             In the large projects, sometimes we may not know the number of arguments to be passed in advance. In such cases, Python provides us the flexibility to provide the comma separated values which are internally treated as tuples at the function call.
                However, at the function definition, we have to define  *variable-name .
                        •	Non–Keyworded Arguments (*args)
                        •	Keyworded Arguments (**kwargs)'''



###  What is the difference between positional arguments and keyword arguments ?

''' ** Positional Arguments are passed in order and must match the funcation's parameters exactly.

    ** Kwyword arguments are passed with names,allowing flexibillity in order.
        Use keyword arguments when the function has many parameters and order doesn't matter.

'''


### How can you make a funcation run at periodic intervals in python ?

'''Use the time.sleep()  method or python schedulerrs like schedule.

        # Example :  
        
        import time

        def repeat_task():
                 while True:
                        print("Running task...")
                        time.sleep(5)  # Pauses execution for 5 seconds

# repeat_task()  # Uncomment to run (It will run forever)

'''

### What are nested funcatins in funcations in python ? Can they access variables from the enclosing funcation ?
'''
 A nested funcation is a funcation defined inside another funcation.
  Yes! Nested funcations can access variables from the enclosing funcation(closure concept)
'''

### What is the difference between mutable and immutable funcation arguments?
'''** Mutable arguments (lists,dictionaries) can be modified inside a funcation
   ** Immutable arguments (integers,strings,tuples) Cannot be changed inside a funcation.
'''

### Whaat is global Funcation ###

'''Local variable has more scope than global variable. 
If we want to access global variable when local and global with same variable name the we use gobal function.'''


### What is the global Keyword in python ?

'''The global keyword allows modifing global variables inside a funcation '''


### What are First-class functions in python ?

'''Funcations in python are First-class objects,meaning:

        * They can be assigned to variables
        * They can be passed as arguments to other funcations
        * They can be returned from funcations
'''
### What is Nested Funcations ###

'''Calling inner functions outside of outer function is not possible to call inner function
    outside of the function'''


### what is Recursive Funcation ###

'''A function that calls by itself is known as recursive function.'''

### Import Funcation ###

'''Import function
In python we can import and export the data.'''

### Lambda Funcation ###

'''
lambda function is a small anonymous function.
Normal function is define using def keyword and lambda function is define using lambda keyword.
A Lambda function can take any number of arguments, but can only have one expression.'''

###Where we exactly use lambda function?  ###
'''Sometime as a programmer we have to pass function as an argument to another function,
   at that particular time we can go for lambda function. These functions mainly used in
   filter(), map(), reduce().'''


### What is Filter Funcation ###

'''The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.'''

#syntax:

'''filter(function, sequence)
        ###function:###
         
                function that tests if each element of a sequence true or not.

                ###sequence:###
                
                sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.

                ###Note: Filter gives the true output only.'''





#### What is the difference between deep copy and Shallow copy ?

'''  ** Shallow Copy copies references (Modifications affect the orginal object)

     ** Deep Copy Creates independent Copies (Chaanges don't affect the original)
'''


### What is Map Funcation ###

'''map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
        
        Syntax :
                  map(fun, iter)
                  
                  fun : It is a function to which map passes each element of given iterable.
                  iter : It is a iterable which is to be mapped.
                  Note: In this some modification on every element.'''


### Wht is reduce Funcation ###

'''The reduce() function receives two arguments, a function and an iterable. However, 
it doesn't return another iterable, instead it returns a single value.
Reduce function present inside the functools, so we have to import it before using reduce function.'''

### Difference between reduce and accumulate ###

'''
reduce gives final output but accumulate gives iterable output
accumulate syntax:(iterable,function)
'''



### What is the difference between map() , filter() , and reduce() , in python

''' ** Map() -- Applies a funcation to each item in an iterable --->  map(lambda x:x*2,[1,2,3])

    ** Filter() -- Filter items based on a condition   ----> filter(lambda x:x > 2,[1,2,3])

    ** Reduce() -- Accumulates values using a Funcation  ---> reduce(lambda x,y:x+y[1,2,3])

        
        from functools import reduce

        numbers = [1, 2, 3, 4, 5]

        # map() - Doubles each number
        doubled = list(map(lambda x: x * 2, numbers))
        print(doubled)  # Output: [2, 4, 6, 8, 10]

        # filter() - Keeps only even numbers
        evens = list(filter(lambda x: x % 2 == 0, numbers))
        print(evens)  # Output: [2, 4]

        # reduce() - Sums up the numbers
        sum_total = reduce(lambda x, y: x + y, numbers)
        print(sum_total)  # Output: 15
    
'''


####  Enumarate Funcation  ####

'''The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
        The enumerate() function adds a counter as the key of the enumerate object.
        
        
    #Syntax:

        enumerate(iterable, start)

        iterable ----------- An iterable object
        start---------A Number. Defining the start number of the enumerate object. Default 0
'''

### Generator Funcation ###

'''A generator-function is defined like a normal function, but whenever it needs to generate a value, 
it does go with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.
        
        ##The difference between the yield and the return statement in Python is:
Return: A function that returns a value at once. The return statement returns a value and exits the function altogether.
Yield: A function that yields values repeatedly. The yield statement pauses the execution of a function and returns a value.
When called again, the function continues execution from the previous yield. A function that yields values is known as a generator.'''



### What is the difference between yield and return ?

'''
**FEATURE               YIELD                                   RETURN
 
 1.Purpose              Produces values one at a time           Sends back a single value
 2.STATE                Keep funcation state intact             Ends funcation execution completely
 3.EFFICIENCE           Saves memory,good for large datasets    Uses stand execution flow


'''
### What is the difference between local and global variable in python ?

''' ** Local variables are declared inside a funcaton and can only be accessed with in the funcation.

    ** Global variable are declared outside any funcation and can be accessed anywhere in the program.
'''





### What is Modules   ###
'''In Python, a module is a file that contains Python code, such as functions, classes, variables, and runnable code.'''

### Requirement:  ###

'''If we want to reuse the code then we go for function, but if we want to reuse group of variables, functions and classes in another file then we go for module.'''


### Types of Modules:  ####

'''1.	Standard Modules or built in Modules

               These modules is already available inside python software.
	Ex: os, sys, math etc
     
   2.	User Defined Modules

                These Modules which is created by user as per requirement.
	Ex: sample, cal etc'
    
   3.	3rd party Modules
   
             These modules provided by 3rd party vendor, it is available on internet so we have to download it by using pip (i.e., pip install numpy) we cannot directly proceed with import.
	Ex: Numpy, pandas, matplotlib etc.   
   
   '''

 
###  Module Aliasing:  ###

'''•	Giving another name to module is called module aliasing
        Ex: import sample as sam'''

###   Module Member Aliasing:   ###

'''•	Giving another name to module member is called module member aliasing.
        Ex: from sample import add as a, sub as s'''















######### FILE HANDLING ###############

'''
File handling is an essantial concept and that allows to you read from and write to file.
Python provide built in funaction to access easy and effective way
'''

# s=open('sample.py' , mode='r')
# print(s.read())
# s.close()

# s=open('sample.py',mode='w')
# s.write('Hello Mani are you there')
# s.close()


# s=open('sample.py',mode='a')
# s.write("bye bye append")
# s.close()


# s=open('sample.py',mode='w+')
# print(s.read())
# s.write("r+ Mode")
# s.close()


# s=open('sample.py',mode='w+')
# print(s.tell())
# s.write('w+ mode')
# print(s.tell())
# s.write('mani')
# s.seek(0)
# print(s.tell())

# print(s.read())
# s.close()

# with open('sample.py','r') as file:
#     s=file.read()
#     print(s)

# with open('sample.py','w') as file:
#     file.write("Thisis writin usimg the 'with' statement.\n")
#     file.write("It will automatically close the file when done.")

# import os

# if os.path.exists('sample.py'):
#     with open('sample.py','r') as file:
#         print(file.read())
# else:
#     print("this file does not exist")



########## OOP #################

'''
Oops means object oriented programming opp is a programming paradaigram to write a programm effectiveli.
in oop we will develop mainly to using class andf object.oop is very sutable for large and complex application 
oop is follow the dry code apporach.
'''

# pop Calculation

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     if b == 0:
#         print("Error! Division by Zero")
#     else:
#         return a/b

# print(mul(10,15))

# oop Calculation

# class Calcilator:
#     def __init__(self,a,b):
#         self.a =a
#         self.b=b
#         self.result=0


#     def add(self):
#         self.result=self.a+self.b
#         return self.result
#     def sub(self):
#         self.result=self.a - self.b
#         return self.result
    
#     def mul(self):
#         self.result=self.a * self.b
#         return self.result
    
#     def div (self):
#         if self.b == 0 :
#             return "error"
#         else:
#             self.result=self.a / self.b
#             return self.result
# cla=Calcilator(10,0)

# print(cla.div())


######## Class And Object##########


# what is class
'''
Class is a blue print of object.it is logical entity and it is virtual and not a real.
if we want to create an object,then we requried a bule perint and that blue print 
is know as class .collection of object is know as Class.
Inside of the class we will represented properities and behaviours     
'''

# what is Object 
'''
Object is a real entity and it isa physical entity.Object is the interface of class.Objects are created inside the head memory
'''

# what is reference variable 

'''
Reference variable is used to refer to an object.Reference variable is acting as an accessor.
Reference variable is used to access properties and methods of an object.
'''


## Example: 1 

# class mani:
#     marks=10 # properitie
        # this is behaviour 
#     def sample(self): # self is the insede of the class reference variable
#         print("helo World")

# s=mani() # s is outside of the class reference variable 

# print(s.marks)
# s.sample()


##Example: 2

# class Student:
#     marks=10 
#     def sample(self,name,age):
#         print(f"my name is {name} and my age is {age}")
# s=Student()
# s.sample("mani",30)


# Example :3 

# class Student :
#     def __init__(self,name,age):  # constractor 

#         self.name =name 
#         self.age=age

#     def details(self):  # inside of the reference variable 

#         print(f"My name is {self.name} ans My age is {self.age}")

# s=Student("Mani",30)  # Out side of the class reference variable 
# s.details()


######### self variable ##########


'''
we can access attributes and methods inside the class.
These variables are used to access instace variables an dinside methods.
Self is used to refer to a current class object or current memory.
'''

# Reference Variable:
 
'''We can access object attributes and methods outside o fthe class '''

# Example 1






###### What is Inheritance ###########
'''Inheritance is a mechanism for creating a new class from an existing class.
Here the old class is called Basw class and the new class is called Derived class.'''


### What is Operator Overloading #####
'''
If we will use same operator in different purpose then it is called operator overloading
'''

### What is Method Overloading ########

'''If 2 or more methods have same name with different no of parameters od different types of 
 parameters is called method overloading
  Python does not support method overloading. Other language like java supports it
  But indirectly we can archieve method overloading by using multiple dispatch decorator
 '''

### What is Method Overloading ########

'''Operator overriding (also called as operator overloding ) is posible in python '''
### What is Method Overriding########
'''
A parent containg some method that method by default available to the child class
If child class wahnt, then child can provide own implementation for those methods,
 This mechianism is called as method overriding 
'''

####### What is constructor overloading ########
'''Constructure overloading is a mechaism in which a class can have any number of constructures
with different no of parameters of different type of paramaters.
Generally it doesnot support but we overcome withh multi dispatch module '''

####### What is constructor overriding ########
'''
Parent class constructure by default avalible to child class,If child class wont satisfy with parent class
then child class can override it
'''

### What is abstraction #########
'''Abstraction means hiding the implementation part and show functionality to the user, this process is called as abstraction.
By using abstract class and interface we can achieve abstraction.
By using interface, we can achieve 100% abstraction whereas by using abstract class we can achieve 0 to 100% abstraction.'''


##### what is interface ######
'''
If the class holds hold only abstract methods then it is know as interface.
Where abstract class  contain abstract as well as constreate method
Pythons doesnot provide any support for interface , so we want define by using abc module
'''