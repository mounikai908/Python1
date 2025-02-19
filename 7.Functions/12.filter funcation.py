'''
The filter() methode filters the given sequence with the help of a funcation that tests each element in th esequence to be true or note .
'''
# SYNTEX ;
'''filter(funcation , sequence)'''
# funcation

'''
funcation that test if each element of a sequence true or not .
'''
# sequence :
'''sequence which needs to be filtered, it can be sets, lists ,tuples, or containers of any iterators'''

## Note : Filter gives the True output only

# WAP to print age is grater than 18 by using filter

# age=[10,20,15,30,18,19]

# def sample(x):
#   if x > 18 :
#       return True
#   else:
#       return False
# adults=filter(sample,age)
# # print(list(adults)) # 1
# for i in adults:#2  Either use 1 or 2 statements to print
#     print(i)

# WAP to print age is greater than 18 by usinf filter with lambda funcation

# age=[10,20,15,30,18,19]

# adults = filter(lambda a : a > 18 , age)
# # print(list(adults))
# for i in adults:
#     print(i)

#WAP to print the vowels is present in the specific elements with filter.

# def sample(a):
#     vowels=['a','e','i','o','u']
#     if a in vowels:
#         return True
#     else:
#         return False
# seq=['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# mani=filter(sample,seq)
# # print(list(mani))
# for i in mani:
#     print(i)

#By using filter with lambda function

# seq=['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# mani=filter(lambda a : a in  ['a', 'e', 'i', 'o', 'u'],seq)
# print(list(mani))

#2nd way using filter with lambda function

# print(list(filter(lambda a:a in ['a','e','i','o','u'], ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'])))


#3rd way using filter with lambda function

# seq=seq=['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# vowels=['a','e','i','o','u']
# result=filter(lambda i :i in vowels,seq)
# # print(list(result))
# for j in result:
#     print(j)

#wap to print even items from dictionary
d={1:"Rama",2:"Krishna",3:"Gopal",4:"Rambabu"}

# print(list(filter(lambda i:i[0] % 2 ==0 ,d.items())))

# for i,j in d.items():
#     if i % 2 ==0 :
#         print(i,j)