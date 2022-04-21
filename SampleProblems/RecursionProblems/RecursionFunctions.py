def factorial(n: int = 0) -> int:
    """
    :param n: number to caluclate factorial of
    :return: integer value of the factorial calculated
    """
    
    if n <= 0:
        return 1
    else:
        product = n*factorial(n-1)
        return product

for i in range(36):
    print("{0} {1}".format(i, factorial(i)))       


def fibonacci(n: int = 1) -> int:
    """
    :param n: the n'th fibonnaci number you want to find
    :return: the n'th fibonnaci number

    This is a recursive solution to finding fibonnaci numbers. =)
    """

    if n == 0:
        fib = 0
    elif n == 1:
        fib = 1
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)

    return fib

for i in range(10):
    print("{0} {1}".format(i, fibonacci(i)))  

def sum_numbers(*args: float) -> float:
    """
    :param *args: list of numbers to sum
    :return: sum of the numbers provided
    """
    final_sum = 0.0

    for a in args:  
        final_sum += a

    return final_sum
    
print(sum_numbers(1,2,3))
print(sum_numbers(8,20,2))
print(sum_numbers(12.5,3.147,98.1))
print(sum_numbers(1.1,2.2,5.5))