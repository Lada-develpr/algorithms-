"""
recursion is a process in which a function calls itself one or more times in its body

this is factorial function that returns the factorial of a number
that is the product of all the integers from one to that number -> O(N)
"""

def factorial(n):
    if n == 0:  # base case
        return 1
    else:  # recursion case
        return n * factorial(n-1)


n = int(input())
print(factorial(n))