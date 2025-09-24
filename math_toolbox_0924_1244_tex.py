# 代码生成时间: 2025-09-24 12:44:24
import numpy as np"""
**Math Toolbox: A collection of mathematical computation tools using NumPy."""

def add(a, b):
    """
    Adds two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of a and b.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divides two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The quotient of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a, b):
    """
    Calculates the power of two numbers.

    Parameters:
        a (float): The base number.
        b (float): The exponent number.

    Returns:
        float: The result of a raised to the power of b.
    """
    return np.power(a, b)

def square_root(a):
    """
    Calculates the square root of a number.

    Parameters:
        a (float): The number.

    Returns:
        float: The square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return np.sqrt(a)

def main():
    # Example usage of the math toolbox functions
    print(add(5, 3))  # Output: 8
    print(subtract(10, 4))  # Output: 6
    print(multiply(2, 7))  # Output: 14
    print(divide(20, 5))  # Output: 4
    print(power(2, 3))  # Output: 8
    print(square_root(25))  # Output: 5.0

def __name__ == "__main__":
    main()
