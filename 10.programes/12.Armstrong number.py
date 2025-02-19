###### Armstrong Number #########

'''
In case of an Armstrog number of 3 digits,the sum of cubes of each digit is equal to the number
itself.
for example: 153 = 1*1*1+5*5*5+3*3*3==153
'''
# number=int(input("Enter number : "))
# sum=0
# for i in range (len(str(number))):
#    cu= int(str(number)[i])**3
#    sum+=cu
# if sum==number:
#     print(number,"is an Armstrong number")
# else:
#     print(number,"is not an Armstrong number")

num=int(input("Enter number : "))
sum=0
tem=num
while tem > 0 :
    d= tem % 10
    sum+= d**3
    tem//=10
# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")