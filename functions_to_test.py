# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    return a + b

def find_maximum(a, b, c):
    return max(a,b,c)

def is_palindrome(string):
    return string == string[::-1]

def count_word_occurrences(text, word):
    try:
        count = text.lower().count(word.lower())
        return count
    except AttributeError:
        raise TypeError("Text must be string")

def read_file_lines(filepath):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        raise FileNotFoundError


def is_prime(n):

    if n == 1:
        return False

    if n<0:
        raise ValueError

    count = 0

    try:
        for i in range(2,n+1):
            if n%i == 0:
                count += 1
    except TypeError:
        raise TypeError
    
    if count == 1:
        return True
    else:
        return False

def sort_numbers(numbers):

    for num in numbers:
        if type(num) != int:
            raise TypeError
    return sorted(numbers)



def factorial(n):
    if n<0:
        raise ValueError
    if type(n) != int:
        raise TypeError
    
    total = 1
    for i in range(1, n+1):
        total *= i
        print(total)
        
    return total

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    numbers = [0,1]

    for _ in range(n-2):
        numbers.append(numbers[-1] + numbers[-2])
    
    return numbers
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


class Person:
    def __init__(self, name, age):
        if type(name) == str:
            self.name = name
        else:
            raise TypeError
        
        if type(age) == str:
            raise TypeError
        else:
            self.age = age


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g