#!/usr/bin/env python3


# Assingment 3 

from functools import *

# 1) a function that calculates the sum of two arguments
def sum(x, y):
    return x + y

# 2) a function that prints m string n times
def print_n_times(n, m = 'null '):
    print(m * n);

# 3) a function that takes 2 argumenst and returns the biggest one
def max(x, y):
    return x if x > y else y

# 4) a functions that returns a 'mirrored' integer
def mirror(num):
    return int(str(num)[::-1])

# 5) a functions that interchanges the first and last digit in a number
def flipLF(num):
    return num if len(str(num)) <= 1 else str(num)[ len(str(num)) - 1 ] + str(num)[1:-1] + str(num)[0] 

# 6) a function that checks if a number if palindrome
def isPalindrome(num):
    return int(str(num)[::-1]) == num
 
# 7) a function that calculates the factorial of a number
def factorial(n):
    return 'Undefined' if n < 0 else reduce(lambda n, k: n * k, [ 1 ] if n <= 1 else range(1, n+1))

# 8) a function that returns the sum of all numbers in a list
def sum(l):
    return reduce(lambda n, k: n + k, l)

# 9) a function that takes ULIMITED arguments and returns the smallest one
def min(*l):
    return reduce(lambda n, k: n if n < k else k, l)

# 10) a function that takes two lists and returns a list that contains unique values from both
def unique(l1, l2):
    return list(set(l1 + l2))

# 11) a function that creates a list of odd numbers of size SIZE, starting with number START
def odd_nums(start, size):
    return list(filter(lambda n: n % 2 == 1, range(start, start + size * 2)))



