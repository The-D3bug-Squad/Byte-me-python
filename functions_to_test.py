# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    return (a+b)

def find_maximum(a, b, c):
     return max(a,b,c) 
     


def is_palindrome(string):
    string = string.replace(" ","")
    reversed_word = string[::-1]
    return string.lower() == reversed_word.lower()

def count_word_occurrences(text, word):
    text.lower().count(word.lower())

def read_file_lines(filepath):
    with open('filepath', 'r') as file:
     file = file.readlines()
    for line in file:
        print(line.strip())


def factorial(n):
 if n == 0:
    return 1
 else:
    return n* factorial(n-1)      


 def is_prime(n):
  pass

def sort_numbers(numbers):
    return sorted(numbers)

def factorial(n):
    pass

def fibonacci(n):
   


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
        pass


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g