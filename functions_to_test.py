# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    if not isinstance(a, (int,float)) or not isinstance(b, (int,float)):
        raise TypeError
    
    return a + b


def find_maximum(a, b, c):
    return max(a,b,c)

def is_palindrome(string):
    if not type(string) == str:
        raise TypeError
    
    return string == string[::-1]

def count_word_occurrences(text, word):
    if type(text) == int:
        raise TypeError
    return text.lower().count(word)

def read_file_lines(filepath):
    with open(filepath, 'r', errors="ignore") as file:
        return file.readlines()

def factorial(n):
    if not isinstance(n, int):
        raise TypeError()
    
    if n < 0:
        raise ValueError()
    
    if n == 0 or n == 1:  
        return 1
    
    return n * factorial(n - 1)


def is_prime(n):
    if not isinstance(n, int):
        raise TypeError()
    
    if n < 0:
        raise ValueError()
    
    if n < 2:
        return False  
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def sort_numbers(numbers):
    for i in numbers:
        if not isinstance(i, int):
            raise TypeError()
        
    return sorted(numbers)

def factorial(n):
    if not isinstance(n, int):
        raise TypeError()
    
    if n < 0:
        raise ValueError()
    
    if n == 0 or n == 1:  
        return 1
    
    return n * factorial(n - 1)


def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError()
    
    if n < 0:
        raise ValueError()
    
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b
    

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
            raise TypeError("Name must be a string.")
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        
        self.name = name
        self.age = age


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g