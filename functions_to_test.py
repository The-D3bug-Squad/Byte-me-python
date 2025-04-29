# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    return a+b
    pass

def find_maximum(a, b, c):
    return max([a,b,c])
    pass

def is_palindrome(string):
    if type(string) == str:
        return True if string.lower() == string.lower()[::-1] else False
    else:
        raise TypeError
    pass

def count_word_occurrences(text, word):
    try:
        return text.lower().count(word)
    except:
        raise TypeError
    pass

def read_file_lines(filepath):
    try:
        with open(filepath, mode = 'r') as file:
            content = file.readlines()
        return content
    except:
        raise FileNotFoundError

import math
def factorial(n):
    if n < 0:
        raise ValueError
    if type(n) == str:
        raise TypeError
    
    if n > 0:
        return math.prod([num for num in range(1,n+1)])
    elif n == 0:
        return 1
    else:
        return ''
        
# print(factorial(0))

def is_prime(n):
    
    if n<0:
        raise ValueError 
        # return ''
    
    elif type(n) == str:
        raise TypeError
    
    elif n == 1:
        return False
    
    for num in range(2,n):
        if n%num == 0:
            return False
    
    return True
    # return True if any([n%num for num in range(2,n)],0) else False
    
    pass

def sort_numbers(numbers):
    if any([True for num in numbers if type(num) == str]):
        raise TypeError
    
    return sorted(numbers)
    
    pass

# def factorial(n):
#     pass

def fibonacci(n):
    if n<0:
        raise ValueError
        
    if n==0:
        return 0
    elif n == 1:
        return 1
    elif n>1:
        num1 = 0
        num2 = 1
        cnt = 1
        while cnt < n:
            new = num1 + num2
            cnt += 1
            num1 = num2
            num2 = new
            
        return num2
    

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
    lst = []
    if n == 0:
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    lst.append((source, target))
    # print(lst)
    tower_of_hanoi(n-1, auxiliary, source, target)
    return lst
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        
        if type(self.name) != str:
            raise TypeError
        if type(self.age) != int:
            raise TypeError

if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    # print(is_prime(8)) #e.g
    print(fibonacci(0))
    print([fibonacci(n) for n in range(15)])
    print(tower_of_hanoi(3, 'A', 'B', 'C'))