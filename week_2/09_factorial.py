def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

print(factorial(5))
#Factorial(n) = n * Factorial(n-1)
#Factorial(n) = n * n-1 * Factoral(n-2)
