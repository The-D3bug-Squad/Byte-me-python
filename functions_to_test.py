# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    return a+b

def find_maximum(a, b, c):
    if a > b and c:
        return a
    elif b > a and c:
        return b
    else:
        return c


def is_palindrome(string):
    pass

def count_word_occurrences(text, word):
    text = text.lower()
    count=0
    for i in text:
        if i == word:
            count+=1
    return count

def read_file_lines(filepath):
    try:
        with open(filepath, "r") as file:
            return file
        
    except FileNotFoundError:
        return print("FILE NOT FOUND!")

    

def factorial(n):
    pass

def is_prime(n):
    if n > 1:
        for i in range(2, (n//2)+1):
            if (n % i) == 0:
                return False
            break
        else:
            return True
    else:
        return True
            

def sort_numbers(numbers):
    n = sorted(numbers)
    
    if (numbers.isdigit()):
        return TypeError
    else:
        return n
def fibonacci(n):
    if n == 1:
        return 1
    
    if n == 0:
        return 0
    else:
         return fibonacci(n-1) + fibonacci(n-2)
    

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