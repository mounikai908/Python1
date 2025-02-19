# Reduce Funcation

'''
The reduce () funcation receives two arguments , a funcation an dan iterable. However ,
It doesn't return another, instead it ruturn a singlr=e value.
Reduce funcation present inside the functools, so we have to import it before using reduce funcation 

'''
# Example 

from functools import reduce

# x=[10,20,30,40,50]

# def sample(a,b):
#     return a+b
# mani=reduce(sample,x)
# print((mani))

# result = reduce(lambda a,b :a+b ,x)
# print(result)

# print(reduce(lambda a,b : a+b , x))

# d={1:"Rama",2:"Krishna",3:"Gopal",4:"Rambabu"}

# result = reduce(lambda a,b :a+b,d.items())
# print(result)

#Difference between reduce and accumulate

'''
Reducec gives final output but accumulate gives iterable output
accumulate syntec:(iterable,funcation)
'''
#reduce example

# a=reduce(lambda a,b:a+b,[2,3,4,5])
# print(a)

# # accunulate example
# from itertools import accumulate
# b = list(accumulate([2,3,4,5],lambda a,b:a+b))
# print(b)