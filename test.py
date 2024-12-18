def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    numbers = [0,1]

    for _ in range(n-2):
        numbers.append(numbers[-1] + numbers[-2])
    
    return numbers

print(fibonacci(15))