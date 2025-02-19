# Map funcation
'''
map() funcation return a map object(which is an iterator ) of th eresults after applying the given funcatioon to each itemof a given iterable (list,tuple etc,.)

Syntex :
map(funcation , sequence(iter))

funcation : It is a funcation to which map passes each element of given iterable
iter(sequence) : It is a iterable which is to be mapped.

note :: In this som emodification on every element.
'''

# Exaample .

# age=[10,20,30,40,50]

# def funcation(n):
#     return n*n

# result=map(funcation,age)
# print(list(result))

# Example by using mp with lambda

# ages=[10,20,30,40,50]

# def sample(a):
#     return a+a
# resul=map(sample,ages)
# print(list(resul))

# print(list(map(lambda i: i+i , ages)))


#Wap to print merging of two lists
# a=[10,20,30,40,50]
# b=[1,2,3,4,5,6]
# print(list(map(lambda i,j: i+j ,a,b)))
# result=map(lambda i,j: i+j,a,b)
# print(list(result))

# def sample (i,j):
#     return i+j
# result=map(lambda i,j : i+j, a,b)
# print(list(result))