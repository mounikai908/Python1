'''
1. Count Vowels and Consonants in a String:

Task: Write a function that takes a string as input and returns the number of vowels and consonants in the string.
Instructions: Use a for loop to iterate through each character in the string and check if it is a vowel ('a', 'e', 'i', 'o', 'u') 
or a consonant. Increment the appropriate counters accordingly.
'''
# name = input("Enter name : ")

# lenth_of_name = len(name)

# vowels ="aeiouAEIOU"
# number_of_vowels = 0
# number_of_consonant =0

# for char in range (lenth_of_name):
#     if name[char] in vowels :
#         number_of_vowels+=1
#     else :
#         number_of_consonant+=1
# print(f"number of vowels in this string {number_of_vowels}\nnumer of consonants in this string {number_of_consonant}")

'''
2. Reverse a String:

Task: Write a function that takes a string as input and returns the string reversed.
Instructions: Use a for loop to iterate through the string backwards,
starting from the last character and appending each character to a new string.
'''

# name = input("enter a name : ")
# revers_string=""
# for i in range(len(name)):
#     revers_string+=name[len(name)-i-1]
# print(revers_string)

'''
2. Sum of Prime Numbers in a Range

Task: Write a program that calculates the sum of all prime numbers within a given range using only for loops.

Instructions:

Define a range of numbers (e.g., between 1 and N).

Use a for loop to check if each number in the range is prime.

Sum all the prime numbers and return the total sum.


Example:

Input: 1 to 20

Output: 77 (Prime numbers are 2, 3, 5, 7, 11, 13, 17, 19)
'''
# number = int(input("Enter Number : "))
# sum_prime_numbers = 0

# for i in range (1,number+1):
#     prime_numbers = 0
#     for j in range(1,i+1):
#         if i % j == 0 :
#             prime_numbers+=1
#     if prime_numbers == 2 :
#         print(i,end=" ")
#         sum_prime_numbers+=i
# print(sum_prime_numbers)

'''
3. Fibonacci Sequence with Custom Range

Task: Write a program that generates a Fibonacci sequence up to a certain number of terms (using for loop) and displays the sequence.

Instructions:

Take the number of terms N as input.

Use a for loop to calculate the Fibonacci numbers and store them in a list.

Display the sequence up to N terms.


Example:

Input: N = 10

Output: 0 1 1 2 3 5 8 13 21 34
'''

'''
4. Pattern Printing

Task: Write a program to print an inverted half-pyramid of stars (*), given the number of rows N.

Instructions:

Use a for loop to print a pattern in the form of a right-angled triangle with stars.

The number of rows will be provided as input, and each row should contain a decreasing number of stars.


Example:

Input: N = 5

Output:

***
**
*
**
*
'''
# number =int(input("Enter NUmuber : "))
# for i in range (number+1):
#     print(" *" * (number-i),"  " * i ,"* " * (number-i))

'''
5. Multiplication Table with Sum

Task: Write a program to generate a multiplication table for a number up to N and also calculate the sum of the products.

Instructions:

Take a number X and an integer N as input.

Use a for loop to print the multiplication table from X * 1 to X * N.

Calculate the sum of all the products in the table and display it.


Example:

Input: X = 3, N = 5

Output:

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
Sum: 45
'''
# x = int(input("Enter number x : "))
# n = int(input("Enter mumber n : "))
# sum_of = 0
# for i in range (1,n+1):
#     sum_of+= x*i
#     print(f"{x} x {i} = {x*i}")
# print(sum_of)

'''
7. Find the Largest Product of Consecutive Numbers

Task: Write a program that finds the largest product of two consecutive numbers in a list.

Instructions:

Given a list of integers, use a for loop to compute the product of consecutive pairs.

Track the largest product encountered.

Return the largest product.


Example:

Input: [1, 2, 3, 4, 5]

Output: 20 (Largest product is 4 * 5)

'''
# N = input("Enter Numbers : ")
# product = 0
# lenth = len(N)
# for i in range (lenth-1) :
#     for j in range(lenth) :
        
#          m = int(N[i]) * int(N[j])
         
#          if product < m :
#             product=m
# print(f"flarge product is {product}")

'''
8. Rotating a List

Task: Write a program that rotates a list by k positions to the right.

Instructions:

Take a list of numbers and a number k.

Use a for loop to rotate the list elements k times to the right.

Output the rotated list.


Example:

Input: [1, 2, 3, 4, 5], k = 2

Output: [4, 5, 1, 2, 3]
'''
#
# for i in range (len(number)) :
#     if i < k :
#         continue
#     else :
#         rotate_list+=(number[i])
# print(rotate_list)
    
# for i in range (1,k+1):
#      rotate_list+=str(number[(-(i))])

# for j in range((lenth)-k):
#      rotate_list+=str(number[j])
# print((rotate_list))  

'''
Task 1: Prime Number Pattern
Instructions: Write a program that prints the first n prime numbers in the following pattern:

The first line will contain the first prime number.
The second line will contain the next two prime numbers.
The third line will contain the next three prime numbers.
Continue this pattern, incrementing the number of primes printed in each line until you've printed n prime numbers.
Sample Input: n = 10

Sample Output:
2
3 5
7 11 13
17 19 23 29
31 37 41 43 47

'''
# number = int(input("Enter Number : "))
# breaking = 0
# prime_numbers =[]
# for i in range (1,1000000):
#      count = 0
#      for j in range (1,i+1):
#           if i % j == 0 :
#                count+=1
#      if breaking == number :
#           break
#      else :
#           if count ==2 :
#                prime_numbers+=str(i)
#                breaking+=1
# print(prime_numbers)

# # for i in range (1,len(prime_numbers)):
# #      print(prime_numbers[i])

'''
Task 4: Reverse Right-Angle Triangle of Numbers
Instructions: Write a program that prints a right-angled triangle pattern in reverse order.
The numbers on each line should start from the line number and count downwards to 1.

Sample Input: n = 5

Sample Output:
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''
# number = int(input("Enter Number : "))
# for i in range (number):
#      N = number -i
#      m=""
#      for j in range (1,N+1):
#           m+=str(j)+" "
#      print(m)
'''

Here are some advanced tasks based on the concept of "for loop" without providing the code but with clear instructions and sample outputs. These exercises will challenge your understanding and use of loops, including nested loops, iterations, and managing complex conditions.

Task 1: Prime Number Pattern
Instructions: Write a program that prints the first n prime numbers in the following pattern:

The first line will contain the first prime number.
The second line will contain the next two prime numbers.
The third line will contain the next three prime numbers.
Continue this pattern, incrementing the number of primes printed in each line until you've printed n prime numbers.
Sample Input: n = 10

Sample Output:

Copy code
2
3 5
7 11 13
17 19 23 29
31 37 41 43 47
Task 2: Fibonacci Sequence Pyramid
Instructions: Write a program that generates a pyramid pattern of Fibonacci numbers. Each row should display Fibonacci numbers, and the number of Fibonacci numbers in each row should increase as the row number increases.

Sample Input: n = 6

Sample Output:

yaml
Copy code
1
1 1
2 3 5
8 13 21 34
55 89 144 233 377
610 987 1597 2584 4181 6765
Task 3: Multiplication Table
Instructions: Write a program that generates a multiplication table of size n x n. The multiplication table should display the product of row and column indices.

Sample Input: n = 5

Sample Output:

Copy code
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
Task 4: Reverse Right-Angle Triangle of Numbers
Instructions: Write a program that prints a right-angled triangle pattern in reverse order. 
The numbers on each line should start from the line number and count downwards to 1.

Sample Input: n = 5

Sample Output:

Copy code
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
Task 5: Diamond Pattern
Instructions: Write a program that prints a diamond pattern using numbers. The upper half of the diamond should start with 1 and increase to n, and the lower half should decrease back to 1.

Sample Input: n = 5

Sample Output:
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1

'''
# number = int(input("Enter Number : "))
# for i in range (1,number+1):
#     a = ""
#     for j in range (1,i+1):
#         a+=str(j)+" "
#         front_space = " " * (number - j)
#     print(front_space,a)
# for c in range (1,number+1):
#     b = ""
#     for d in range (1,number-c+1):
#         b+=str(d)+" "
#         _space = " " * (number - d)
#     print(_space,b)
    
'''
Task 6: Nested Star Pyramid
Instructions: Write a program that prints a pyramid of stars (*),
with the first row containing one star, the second row containing three stars, and so on, 
increasing by two stars per row, until the total rows equal n.

Sample Input: n = 5
    *
   ***
  *****
 *******
*********

'''
'''# i = 0
# j = int(input("Enter how many prime numbers you required : "))
# is_prime = 1
# mani=[1]
# while i < (j-1) :
#     counts = 0
#     for a in range (1,is_prime+1):
#         if is_prime % a == 0 :
#             counts+=1
#     if counts == 2 :
#         mani.append(is_prime)
#         i+=1
#     is_prime+=1
# print(mani)
# for A in range (j):
#     space=" " * (j -A)
#     print(space,"*" * mani[A])
n = 1
number = int(input("Enter number : "))
for i in range (number):
    space = " " * (number-i)
    stars = "*" * n
    print(space,stars)
    n+=2 '''
    
'''
25. Rotate a List Left by K Positions

Task: Write a program that rotates a list to the left by k positions.

Instructions:

Given a list and a number k, use a for loop to move the elements of the list to the left k positions.

Ensure that the elements at the front of the list wrap around to the end.

Return the rotated list.


Example:

Input: list = [1, 2, 3, 4, 5], k = 2

Output: [3, 4, 5, 1, 2]

'''

# list = eval(input("Enter list : ")) # take input from user as a list
# k = int(input("Enter k value : ")) # how many values are rotate 
# for i in range (k):
#     list.append(list[0]) # rotate list elements 
#     list.pop(0) # remove elements 
# print(list)

'''

26. Check if Two Strings are Anagrams

Task: Write a program to check if two strings are anagrams of each other using for loops.

Instructions:

Take two strings as input.

Use for loops to check if both strings have the same characters in any order.

Ignore spaces and case.

Return True if the strings are anagrams, otherwise return False.


Example:

Input: "listen", "silent"

Output: True
'''
# name1 = input("Enter name 1: ").strip().lower # take input from user 1
# name2 = input("Enter name 2 : ").strip().lower# take input from user 2
# name = ""
# # for i in name1 :
# #     for j in name2:
# #         if i.lower == j.lower :
# #             name+= j
# # if name1.lower == name.lower:
# #     print(True)
# # else:
# #     print(False)
# print(name1,name2)


'''

27. Find Missing Number in List (1 to N)

Task: Write a program to find the missing number in a list that contains all integers from 1 to N except one.

Instructions:

Given a list of numbers ranging from 1 to N with one number missing, use a for loop to find and return the missing number.

Assume the list contains no duplicates.


Example:

Input: list = [1, 2, 4, 5], N = 5

Output: 3
'''
# list1=eval(input("Enter list : ")) # take  list from 1 to n numbes miss one or more numbers 
# # lst =list(map(int, list1.split()))
# n = int(input("Enter numbers : ")) # take a rane numbers from 1 to n
# for i in range (1,n+1): 
#     if i in list1: # check missing number
#         pass
#     else :
#         print(i,end=' ') # print missing number 

'''

'''

# number = int(input("Enter number : "))

# for i in range (1,number+1):
#     mani = ''
#     for j in range (1,number+1):
#          if i == 1 or i == number :
#              mani+=str(j)+" " 
#          else :
#             mani=(str(1)+" " + "  " * (number-2) + str(number))
#             pass
#     print(mani)

# # number = int(input("Enter Number : "))
# # for i in range (1,number+1):
# #     print(" " * (number-i), "* " * i)

'''

2. Sum of Prime Numbers in a Range

Task: Write a program that calculates the sum of all prime numbers within a given range using only for loops.

Instructions:

Define a range of numbers (e.g., between 1 and N).

Use a for loop to check if each number in the range is prime.

Sum all the prime numbers and return the total sum.

Example:

Input: 1 to 20

Output: 77 (Prime numbers are 2, 3, 5, 7, 11, 13, 17, 19)
'''
# ## sum of prime numbers 1 to n numbers  only using for loop concepet
# number = int(input("Enter Number : ")) # take input from user 
# sum_of_primeNumbers=0 # sum of prime numbers 
# for i in range (2,number+1):
#     is_prime = 0
#     for j in range (1,i+1): # generate numbers from 1 to n numbers
#         if i % j == 0 : # check i divisible by j 
#             is_prime+=1
#     if is_prime == 2 : # check prim enumber 
#         sum_of_primeNumbers+=i
# print(f"Total sum of prime numbers 1 to {number} is = {sum_of_primeNumbers}") # print output

'''

Task: Write a program to reverse a string without using slicing, but only using a for loop.

Instructions:

Take an input string and reverse it using a for loop.

Output the reversed string.

Example:

Input: Hello

Output: olleH
'''
# name = input("Enter name : ") # take input from user
# reverse_string = '' # reverse string 
# for i in range(len(name)):
#     reverse_string+=name[len(name)-i-1]
# print(reverse_string) # print output

'''
7. Find the Largest Product of Consecutive Numbers

Task: Write a program that finds the largest product of two consecutive numbers in a list.

Instructions:

Given a list of integers, use a for loop to compute the product of consecutive pairs.

Track the largest product encountered.

Return the largest product.

Example:

Input: [1, 2, 3, 4, 5]

Output: 20 (Largest product is 4 * 5)
'''
# list1 = eval(input("enter list: "))
# product=0
# for i in list1:
#     for j in range (1,len(list1)-1):
#         m= i * list1[j]
#         if product < m :
#             product=m
# print(product)

'''
9. Count Vowels and Consonants in a String

Task: Write a program that counts the number of vowels and consonants in a given string.

Instructions:

Define a string and iterate through it using a for loop.

Count how many vowels (a, e, i, o, u) and consonants are present in the string.

Output the counts.

Example:

Input: "Hello World"

Output: Vowels = 3, Consonants = 7
'''
# name = input("Enter sentange :  ") # take input from user 
# vowels = "aeiouAEIOU"
# vowels_count=0
# consonants = 0
# for char in name :
#     if char in vowels :
#         vowels_count+=1
#     elif char.isalpha():
#             consonants+=1
# print(f"number of vowels in this string = {vowels_count}\nnumber of consonant is this string = {consonants}")

'''
10. Pascal's Triangle

Task: Write a program to generate Pascal’s Triangle up to n rows using for loops.

Instructions:

Generate Pascal’s Triangle where the first row is 1 and each subsequent row is formed by adding adjacent numbers from the row above.

Output the triangle in a readable format.

Example:

Input: n = 5

Output:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''


'''
11. Find the Longest Substring Without Repeating Characters

Task: Write a program to find the length of the longest substring without repeating characters in a given string.

Instructions:

Given a string, use a for loop to iterate through the string and track the characters in the substring.

Ensure that no character repeats in the substring and calculate its length.

Return the length of the longest substring found.

Example:

Input: "abcabcbb"

Output: 3 (Longest substring without repeating characters is "abc")
'''
# string=input("Enter stering : ")
# large=''
# for cha in string:
#     if cha in large:
#         continue
#     else:
#         large+=cha
# print(large)

'''
12. Count Digits, Letters, and Special Characters

Task: Write a program that counts the number of digits, letters, and special characters in a given string.

Instructions:

Use a for loop to iterate through the string.

Track how many digits, alphabetic characters, and special characters (non-alphabetic, non-digit characters) exist in the string.

Output the counts for each category.


Example:

Input: "Hello World! 123"

Output:

Digits: 3

Letters: 10

Special Characters: 2
'''
# name = input("Enter mixed string : ")
# number_of_digits=0
# number_of_letters=0
# number_of_specialchar=0
# for char in range(len(name)):
#     if name[char].isnumeric:
#         number_of_letters+=1
#     elif name[char].isalpha :
#         number_of_digits+=1
#     else:
#         if name[char] == " ":
#             continue
#         else:
#             number_of_specialchar+=1
# print(f"number of degits in this string = {number_of_digits}\nnumber of latters in this string = {number_of_letters}\nnumber of special characters in this string = {number_of_specialchar}")
# print(len(name))

# number = int(input("Enter NUmber : "))
# b=""
# for i in range (1,number+1):
#     a=""
    
#     for j in range (1,i+1):
#         if j==1 or j == i :
#             a+="1 "
#         else : 
#             # for k in b :
#             #     if k.isnumeric:
#             #         pass
#            a+=str(j)  + " "       
#         # a+=str(j)+" "
#     b=a
#     print(a)
#     # print(a)

# def generate_pascals_triangle(num_rows):
#     triangle = []

#     for i in range(num_rows):
#         row = [1] * (i + 1)
#         for j in range(1, i):
#             row[j] = triangle[i-1][j-1] + triangle[i-1][j]
#         triangle.append(row)

#     return triangle

# # Take input from the user for the number of rows
# num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))

# # Generate Pascal's Triangle
# pascals_triangle = generate_pascals_triangle(num_rows)

# # Print Pascal's Triangle
# for row in pascals_triangle:
#     print(row)

num = 1

while num <= 100:

    num += 1

    i = 2

    is_prime = True

    while i  <= num:

        if num % i == 0:

          is_prime = False

          break

          i += 1

if is_prime and num > 1:
    print(num)