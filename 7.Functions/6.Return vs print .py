#### RETURN vs PRINT ####
'''
In funcations internally return a value by default as none 
'''
# Example 

# def add(a):
#     print(a)
    
# print(add(10)) # Here it will return None because we not returning any thing .

# def add (a):
#     print(a) #10
#     return a-5
# print(add(10)) #5

# def add():
#     list=[10,20,30]
#     return list
# print(add())

# def sample():
#     print("Hello")
#     return 10
# print(sample()) # return replace None values.

'''
return statement only be at end of the funcation.
If we  give return statement in thh emiddle after return statement
remaining statement will not going to be executed .
'''

# def sample(a,b,c):
#     return a,b,c
# print(sample(10,20,30))