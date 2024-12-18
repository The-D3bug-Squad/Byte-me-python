# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    return a + b


def find_maximum(a, b, c):
    return max(a, b, c)


def is_palindrome(string):
    if type(string) == type("stirng"):
        if string == string[::-1]:
            return True
        else:
            return False
    else:
        raise TypeError("Invalid input!")
    

def count_word_occurrences(text, word):
    if type(text) == type(word):
        text = text.upper()
        word = word.upper()
        count = text.count(word)
        return count
    else:
        raise TypeError("Invalid type entered")
    

def read_file_lines(filepath):
    try:
        with open(filepath, "r") as f:
            file = f.readlines()
    except FileNotFoundError as e:
        print(e)


def factorial(n):
    fact = n

    if type(n) != type(0):
        raise TypeError("Invalid type!")
    elif n == 0:
        return 1
    elif n < 0:
        raise ValueError("Invalid number!")
    for i in range(1, n):
        fact = fact * i
    return fact


print(factorial(0))

def is_prime(n):
    count = 0
    if type(n) == type(0):
        if n == 1:
            return False
        elif n < 0:
            raise ValueError("Prime not defined for negative numbers")
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        if count > 2:
            return False
        else:
            return True
    elif type(n) != type(0):
        raise TypeError("Invalid input!")


def sort_numbers(numbers):
    if numbers == []:
        return []
    for i in numbers:
        if type(i) == type(0):
            return sorted(numbers)
        else:
            raise TypeError("Invalid list elements")


def fibonacci(n):
    fibo_list = [0, 1]

    for i in range(n - 1):
        fibo_list.append(fibo_list[len(fibo_list) - 2] + fibo_list[len(fibo_list) -1])

    return fibo_list[n]

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
        self.name = name
        self.age = age

        if type(name) != type("string"):
            raise TypeError
        if type(age) != type(0):
            raise TypeError


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g