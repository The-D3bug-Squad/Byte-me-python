# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    return a+b

def find_maximum(a, b, c):
    return max(a,b,c)

def is_palindrome(string):
    return string[::-1] == string

def count_word_occurrences(text, word):
    return text.count(word)

def read_file_lines(filepath):
    counter = 0
    with open(filepath, "r") as file:
        for line in file.readline():
            counter += 1
    return counter
            

def factorial(n):
    try:
        counter = 1
        if n < 0:
            raise ValueError
        elif n == 0 or n == 1:
            return counter
        else:
            for i in range(n, 1, -1):
                counter *= i
            return counter
    except TypeError:
        pass

def is_prime(n):
    if n < 0 :
        raise ValueError
    else:
        counter = 0
        for i in range(1, n+1):
            if n % i == 0:
                counter += 1
        if counter == 2:
            return True
        else:
            return False

def sort_numbers(numbers):
    try:
        for i in numbers:
            if i is int:
                if numbers == []:
                    return []
                else:
                    return sorted(numbers)
            else:
                raise TypeError
    except TypeError:
        pass
        
def factorial(n):
    counter = 1
    if n < 0:
        return ""
    elif n == 0 or n == 1:
        return counter
    else:
        for i in range(n, 1, -1):
            counter *= i
        return counter

def fibonacci(n):
    if n == 0:
        return None
    if n == 1:
        return 0
    else:
        list_of_fib = list()
        a, b = 0, 1
        for _ in range(n):
            list_of_fib.append(a)
            a, b = b, a + b
        return list_of_fib[-1]
        


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


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g
    print(factorial(0))
    # print(sort_numbers([-3, -1, -2]))
    print(fibonacci(5))
    print(is_prime(3))
    print(factorial(9))
    print(read_file_lines("database.csv"))