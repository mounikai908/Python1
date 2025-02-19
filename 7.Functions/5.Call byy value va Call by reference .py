### Call by value vs call by reference

##########  call bye value  ##########

'''
if we made any changes on called funcation it will not refelact on outside the funcation
When we called eith value.
'''
# def sample(a): # Called funcation
#     print("This is inside the funcation before modification : ",a )
#     print("This is inside of the funcation before modifcation of id : ",id(a))
#     a=30 # Here we cannot append because in is immutabule 
#     print("this is inside of the funcation after modification : ",a)
#     print("This is inside of the funcation after modification id : ",id(a))

# a=20
# print("This is outside of the funcation before calling : ",a)
# print("this is outside of the funcation before calling id : ",id(a))
# sample(a) # calling funcation
# print("This is the outside of the funcation after calling : ",a)
# print("This is outside of the funcation after calling id ; ",id(a))


##### call by reference ########
'''
If we made any changes on called funcation it will refelact on outside the funcation we call with reference. 
'''
# def sample(a): # called funcation 
#     print("This is inside of the funcation before modification : ",a)
#     print("This is inside of the funcation before modification id : ",id(a))
#     a.append(40) 
#     print("this is inside of the funcation after modification : ",a)
#     print("This is the inside of the funcation after modification id : ",id(a))
# a=[20,30,10] # Here list is mutable
# print("This is out side of the funcation before calling : ",a)
# print("This is out side of the funcation before calling id : ",id(a))
# sample(a) # calling funcation
# print("This is out side of the funcation after funcation calling : ",a)
# print("This is the out side of the funcation after funcation calling id : ",id(a))

#### NOTE ##########

'''
Python does not support call by value or call by reference it support by call by object reference.
 When we pass immutiable object like int , float , tuple , it acts like call by value (i.e modify that object and create new object.)
 and when we pass mutuble objects like list , dictionary its acts like call by reference (i.e modify that object and will not create new object.).
'''