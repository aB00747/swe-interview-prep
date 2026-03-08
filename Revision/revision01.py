# Basic Math Problems

# Reverse the Number
def revNum(num: int) -> int:
    """
    Reverse the digits of an integer.
    This function takes a positive integer and returns a new integer with its digits reversed.
    For example, 12345 becomes 54321.
    Args:
        num (int): A positive integer to be reversed.
    Returns:
        int: The reversed integer.
    Example:
        >>> revNum(12345)
        54321
        >>> revNum(100)
        1
        >>> revNum(9)
        9
    """
    rev = 0

    while num > 0:
        lastDigit = num % 10
        rev = rev * 10 + lastDigit
        num = num // 10

    return rev

print(revNum(12345))

def palNum(num: int) -> bool:
    """
    Check if a number is a palindrome.
    This function takes a positive integer and determines whether it reads the same
    forwards and backwards. For example, 121 is a palindrome, but 123 is not.
    Args:
        num (int): A positive integer to check if it is a palindrome.
    Returns:
        bool: True if the number is a palindrome, False otherwise.
    Example:
        >>> palNum(121)
        True
        >>> palNum(12321)
        True
        >>> palNum(123)
        False
    """
    wholeNum = num
    result = 0

    while num > 0:
        ld = num % 10
        result = result * 10 + ld
        num = num // 10

    return wholeNum == result

print("palNum", palNum(121))

# Amstrong Numbers
def armstrongNum(num: int) -> int:
    """
    Check if a number is an Armstrong number (Narcissistic number).
    An Armstrong number is a number that is equal to the sum of its own digits
    each raised to the power of the number of digits. This function specifically
    checks for 3-digit Armstrong numbers (each digit cubed).
    Args:
        num (int): The number to check if it is an Armstrong number.
    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    Example:
        >>> armstrongNum(153)
        True
        >>> armstrongNum(370)
        True
        >>> armstrongNum(100)
        False
    Note:
        This implementation is hardcoded for 3-digit numbers (power of 3).
        For a generalized solution, the power should be dynamically determined
        based on the number of digits in the input number.
    """
    result = 0
    original = num

    while num > 0:
        lastDigit = num % 10
        result += pow(lastDigit, 3)
        num = num // 10

    return result == original

print(armstrongNum(153))

# Eculirean Algorithm
def gcd(n1: int, n2: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    This function recursively computes the GCD of two non-negative integers by repeatedly
    subtracting the smaller number from the larger number until one of them becomes zero.
    Args:
        n1 (int): The first non-negative integer.
        n2 (int): The second non-negative integer.
    Returns:
        int: The greatest common divisor of n1 and n2.
    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(100, 50)
        50
        >>> gcd(17, 19)
        1
    Note:
        This implementation uses the subtraction-based Euclidean algorithm.
        For better performance with large numbers, consider using the modulo-based approach.
    """

    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1

    if n1 > n2:
        return gcd(n1 - n2, n2)
    else:
        return gcd(n2 - n1, n1)

print(gcd(20, 15))

def gcd2(a: int, b: int) -> int:
    if b == 0:
        return a
    
    return gcd2(b, a % b)

print(gcd2(20, 15))

def revStr(str: str) -> str:
    rev = ''
    n = len(str)

    for i in range(n - 1, -1, -1):
        rev += str[i]

    return rev
print("simple rev string", revStr("XYZS"))

def revStr2(str: str) -> str:
    return str[::-1]

print("rev string 2 with range", revStr("XYZS"))

revStrLambda = lambda s: s[::-1]

print("revStrLambda String", revStrLambda("ABCD"))