def factorialRecursion(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
        
print (factorialRecursion(3))