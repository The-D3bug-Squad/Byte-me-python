# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    return a+b

def find_maximum(a, b, c):
    maximum=[a,b,c]
    return max(maximum)

def is_palindrome(string):
    if string==string[::-1]:
        return True
    else:
        return False

def count_word_occurrences(text, word):
    
    if isinstance(text, int):
        raise TypeError
    else:
        count=0
        word1=text.lower()
        for i in word1.split():
            if i == word :
                count+=1
        return count
        

def read_file_lines(filepath):
    with open(filepath,'r') as f:
        the=f.read().split()

    return the

def factorial(n):
    if n<0:
        raise ValueError
    elif isinstance(n, str):
        raise TypeError
    else:
        # count=1
        # if n==0:
        #     return count
        # else:
            # for i in range(n+1):
            #     count*=i
        return n


def is_prime(n):
    if n<0:
        raise ValueError
    elif isinstance(n, str):
        raise TypeError
    else:
        count=0
        for i in range(2,n):
            if n%i==0:
                count+=1
        if n==1:
            return False
        elif count>0:
            return False
        else:
            return True

def sort_numbers(numbers):
    if len(numbers)>0:
        for i in numbers:
            if isinstance(i,str):
                raise TypeError
            else:
                return sorted(numbers)
    else:
        return numbers

def factorial(n):
    pass

def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        count=[0,1]
        for i in range(n):
            num=count[-1]+count[-2]
            count.append(num)
        return count

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
        if isinstance(name,str) and isinstance(age,int):
            self.name=name
            self.age=age
        else:
            raise TypeError


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g