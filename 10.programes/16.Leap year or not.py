## Python program to check if year is a lep year or not

# year=int(input("Enter Year : "))

# if year % 400==0 and year%100==0:
#     print("{0} is a leap year".format(year))
# elif year % 4 == 0 and year % 100 !=0:
#      print("{0} is a leap year".format(year))
# else:
#     print("{0} is not a leap year".format(year))


year=int(input("Enter Year : "))

if (year%400==0)and(year%100==0) or (year%4!=0):
    print(f"{year} is a century leap year.")
elif year % 400 == 0 and year % 100 ==0 :
     print(f"{year} is a  leap year.")
elif year % 4 == 0 and year%100 !=0:
    print(f"{year} is a  leap year.")
else:
    print(f"{year} is not a leap year.")