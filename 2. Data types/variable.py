# DATA TYPES
'''
Classification of a variable which deals with type of a variable
    TYPES OF DATA TYPES
         NUMBER DATATYPES
            1. integer(int)1,2,3,4,5,6.......
            2.float(float)1.0,2.0,3.0,3.3,3.5,3.25.........
            3.complex 2+3j,2+3h.....
            4.boolen(bool) true , fales
        COLLECTION DATA TYPE
            1.list[]
            2.tuple()
            3.set{}
            4.dict{}

'''
"""
how to identify variable tye 
 we can use to identifi variable type - type(variable)
    1.  a = 10
        print(f"value of a is {a}")
        print(f"{type(a)}")
    2.  a = 10.0
        print(f"value of a is {a}")
        print(f"{type(a)}")
    3.  a = "10"
        print(f"value of a is {a}")
        print(f"{type(a)}")
"""
# complex
"""
a=24+2j
print(a)
print(f"{a.real}and type {type(a.real)}")
print(f"{a.imag}and type {type(a.imag)}")
"""
# TYPE CONVERSATION
'''
# to convert one data type into another daata type is called type conversation
    1.  a = 24                              # this is int value
        print(f"{type(a)}")                 # know type of variable type
        print(f"{float(a)}")                # convert int to float
        print(f"{type(float(a))}")          # know type of a variable
'''
# TO GIVE DATA IN RUN TIME
'''
    1.  hie_tech = int(input("enter how many students are there :")) # tack input value in int 
        print(f"NUmber of students are {hie_tech}")                 # Use f-string print option

    2.  hie_tech = input("enter name of the student :") # tack input value in string 
        print(f"Name of student is {hie_tech}")                 # Use f-string print option

    3.  hie_tech = float(input("enter percentage of the student :")) # tack input value in float (in this case you can't take interger value you can tack only float value)
        print(f"Percentage  of student  {hie_tech}")                 # Use f-string print option   
'''
  