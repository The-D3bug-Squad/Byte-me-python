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
    pass

def is_prime(n):
    try:
        if type(n) == type(0):
            outcome = is_prime(n)
            return outcome
    except TypeError as e:
        print(e)
    except RecursionError as e:
        print(e)
    
def sort_numbers(numbers):
    try:
        if type(numbers) == type([]):
            return sorted(numbers)
    except TypeError:
        print("invalid type")

def factorial(n):
    pass

def fibonacci(n):
    fibo_list = [0, 1]

    for i in range(n - 1):
        fibo_list.append(fibo_list[len(fibo_list) - 2] + fibo_list[len(fibo_list) -1])

    return fibo_list[n]
    
    
print(fibonacci(15))

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