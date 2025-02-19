#Variable is the name of address where data will be stored in it
#Data means Raw material of requires information 
# variable name can use max 32 characters
'''
We can declare a variable with alpha numeric char
mani=100
print(mani)
    or
Mani=100
print(Mani)
    or
Mani123=100
print(Mani123)
'''
#we can't declare a variable starting with numbers
'''
123mani=1000
print(123mani)
    or
12345=1000
print(12345)
'''
# If we want to declare a variable with number ther use underscore(_)
'''
_1234=100
print(_1234)
    or
_mani1234=100
print(mani1234)
'''
# variable name should not be tack two words
'''
mani kolla =100
print(mani kolla)
'''
# If we want to declare a varible with two or more words then give underscore(_) between those words
'''
mani_kolla = 100
print(mani_kolla)
'''
# IDE - INTEGRATED DEVELOPMENT ENVIRONMENT 
'''
we can give a variable with one data in multiple lines
a = 100
b = 200
c=a+b
print(c)
'''
'''
we can give multiple variable give a sinhle line every variable devided with camma(,)
a,b,c,d = 1,2,3,4
print(a,b,c,d)
'''
'''
we can give different variables in single line and give a single data every variable seperated by equaltwo(=)
a=b=c=10
print(a)
print(b)
print(c)
'''
# variables are two types 1. globle variable and 2.  local variable
'''
t=77                  - this is globle variable
def sample ():       - this is called funcation
    t=24             - this is called local variable
    print(t)
sample()             -  this is calling funcation
    in this case print locall value 

in the above program we can't give sample () then no out put 
M=100
def mani ():
    M=101
    print(mani)
     
    in this case ther is no out put
'''
# we can change global value in local value 
'''M = 100
def mani():
    global M
    M = 200
    print(M)
mani()
print(M)
'''
# Different types of printing methods
'''
1.      name = "mani"
        age = 24
        print(name,age)
'''
'''
2.      name = "mani"
        age = 24
        print("my name is :",name,"my age is :",age)
'''
''' this is called f_string
3.      name = "mani"
        age = 24
        print(f"my name is {name} and my age is {age}")
'''
'''
4.      name = "mani"
        age = 24
        print("my name is %s and my age is %d"%(name,age))
'''
'''
5.      name ="mani"
        age = 24
        print("my name is {}and my age is {}".format(name ,age))
'''

# cmp(tuple1,tuple2)
t1=(50,60,70,80)
t2=(50,60,76,80)
print(t1==t2)
print(t1<t2)
