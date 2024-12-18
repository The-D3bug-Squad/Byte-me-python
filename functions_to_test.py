# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError
    
    try:
        sum = a + b
        return sum
    except:
        raise TypeError

def find_maximum(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        raise TypeError
    
    try:
        high = max(a,b,c)
        return high
    except:
        TypeError

def is_palindrome(string):
    try:
        if type(string) != str:
            raise TypeError
        
        string = string.replace(" ","")
        reversed_word = string[::-1]
        return string.lower() == reversed_word.lower()
    except:
        raise

def count_word_occurrences(text, word):
    try:
        if type(text) != str or type(word) != str:
            raise TypeError
        text = text.lower()
        word = word.lower()
        list1 = text.split()
        return list1.count(word)
    except:
        raise

def read_file_lines(filepath):
    try:
        if type(filepath) != str:
            raise TypeError
        with open(filepath, 'r') as f:
            return f.readlines()
    except:
        raise

def factorial(n):
    try:
        if type(n) != int:
            raise TypeError
        if n < 0:
            raise ValueError
        if n == 0:
            return 1
        result = 1
        for i in range(1,n +1):
            result *= i
        return result
    except:
        raise
        
    

def is_prime(n):
    try:
        if type(n) != int:
            raise TypeError
    
        if n < 0:
            raise ValueError
        if n < 2:
            return False
        number = int(n ** 0.5) + 1
        for j in range(2,number):
            if n % j == 0:
                return False
        return True
    except:
        raise

def sort_numbers(numbers):
    try:
        for x in numbers:
            if type(x) != int:
                raise TypeError
    except:
        raise
    
    return sorted(numbers)

def factorial(n):
    try:
        if type(n) != int:
            raise TypeError
        if n < 0:
            raise ValueError
        
        result = 1
        for i in range(1,n +1):
            result *= i
        return result
    except:
        raise

def fibonacci(n):
    try:
        if type(n) != int:
            raise TypeError
        if n < 0:
            raise ValueError
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        x,z = 0,1
        for _ in range(2, n+1):
            x,z = z, x +z
        return z
    except:
        raise

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
        try:
            if type(name) != str:
                raise TypeError
            if type(age) != int:
                raise TypeError
            
            self.name = name
            self.age = age
        except:
            raise

if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g