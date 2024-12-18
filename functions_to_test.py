# Placeholder functions for Python basics, to be implemented later
import math


def add_numbers(a, b):
    return(a+b)


def find_maximum(a, b, c):
    list1 = [a,b,c]
    return(max(list1))
print(find_maximum(4,5,6))

def is_palindrome(string):
    if type(string) == str:
        string = string.lower()
        string1 = string[::-1]
        return(string==string1)
    else:
        raise TypeError

def count_word_occurrences(text, word):
   if type(word) == str and type(text) == str:
        text1 = text.lower()
        word1= word.lower()
        word_count = text1.count(word1)
        return (word_count)
   else:
       raise TypeError

            

def read_file_lines(filepath):
    with open(filepath,"r") as file:
        lines = file.readlines()
        return(lines)

def factorial(n):
    if n < 0:
        raise ValueError
    elif type(n) != int:
        raise TypeError
    from math import factorial as factors
    return factors(n)


def is_prime(n):
    if n < 0 :
        raise ValueError
    elif n <= 1:
        return False
    elif type(n) != int :
        raise TypeError
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
    
    

def sort_numbers(numbers):
    for i in numbers:
        if type(i) == str:
            raise TypeError
    return sorted(numbers)

def factorial(n):
    if n < 0:
        return ""
    elif type(n) != int:
        raise TypeError
    from math import factorial as factors
    return factors(n)

def fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1  
    return(fibonacci(n-1)+fibonacci(n-2))

def tower_of_hanoi(n, source, auxiliary, target):
    
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    pass

class Person:
    def __init__(self, name, age):
        if type(name) == str and type(age) == int:
            self.name = name
            self.age = age
            return
        else:
            return TypeError


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g