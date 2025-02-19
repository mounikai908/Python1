# Lambda funcation


'''
lambda funcation isa small anonymous funcation.
Normal funcation is define using de keyword and lambda is define using lambda keyword.
A lambda funcation can take any number arguments, but can only have one expression.
'''
# x=lambda a,b,c:a+b 
# print(x(1,8,3))

# print((lambda a,b,c : a+b ) (10,22,33))

# Example

# x= lambda n:n*n
# print(x(5))

# print((lambda n:n*n)(10))

# y= lambda a,b:a if a > b  else b 

# print(y(10,20))

# print((lambda a,b :a if a > b else b) (10,20))

# Example 

# z= lambda a,b : a,b # error because lambda can take any no oof arguments but have only one expression
# print(z(10,20)) 

# z=lambda a,b:(a,b) # Here it is one expression
# print(z(10,20)) # It works Because it is one expression with inone entity tuple

## Where we exctly use lambda funcation 
'''
Sometimes as a programmer we have to pass funcation as an argument to anoher funcation ,
at that particular time we can go for lambda funcation mainly used in filter(), nap(),reduce.
'''