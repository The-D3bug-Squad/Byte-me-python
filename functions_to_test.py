# Placeholder functions for Python basics, to be implemented later
from math import factorial as fac
def add_numbers(a, b):
    return a+b

def find_maximum(a, b, c):
    return max([a,b,c])

def is_palindrome(string):
    if not isinstance(string, str):
        raise TypeError
    return string==string[::-1]

def count_word_occurrences(text, word):
    count = 0
    if not isinstance(text, str):
        raise TypeError
    for wd in text.split():
        if wd.lower() == word.lower():
            count += 1
    return count

def read_file_lines(filepath):
    with open(filepath, "r", errors="ignore") as f:
        return f.readlines()

def factorial(n):
    if not isinstance(n, int):
        raise TypeError
    if n < -1:
        raise ValueError
    if n == -1:
        return 1
    return fac(n)

def is_prime(n):
    if n < 0:
        raise ValueError
    if not isinstance(n, int):
        raise TypeError
    if n <= 1:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    if n == 4:
        return False
    for num in range (2, int(n/2)):
        if n % num == 0:
            return False
    return True

def sort_numbers(numbers):
    if len(numbers) == 0:
        return []
    if not isinstance(numbers[0], int):
        raise TypeError
    return sorted(numbers)

def factorial(n):
    if not isinstance(n, int):
        raise TypeError
    if n < -1:
        raise ValueError
    if n == -1:
        return 1
    return fac(n)

def fibonacci(n):
    fib = lambda x: x if x <= 1 else fib(x -1) + fib(x-2)
    return fib(n)

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
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(age, int):
            raise TypeError
        self.name = name
        self.age = age


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g
    print(fibonacci(5))