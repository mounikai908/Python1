####### Global funcation

# Local variable has more scope then global variable . if we want to access global variable when local vand global name the we use gobal funcation

# a=10
# def sample():
#     a=20
#     print(a)
# sample()

# a=10
# def sample():
#     a=20
#     print(a)
#     print(globals()["a"])
# sample()

#######  Nested Funcations

'''
Calling inner funcation outside of touter funcation is not possible to call inner funcation outside of the funcation 
'''

# def Outr_fun():
#     print("Inside outer funcation")
    
#     def inner_fun():
#         print("Inside inner funcation")
#     inner_fun()
# Outr_fun()
# # inner_fun() # error

# def outer_fun():
#     print("Inside outer funcation")
#     def inner_fun():
#         print("Inside inner funcation")
#     return inner_fun

# x=outer_fun() # when outr funcation is equal to some variable then it returns inner funcation as well

# x()

'''
Output:
Inside outer function
Inside inner function
'''