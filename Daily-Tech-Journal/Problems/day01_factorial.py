def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

# Example
n = 5
print("Iterative:", factorial_iterative(n))
print("Recursive:", factorial_recursive(n))
