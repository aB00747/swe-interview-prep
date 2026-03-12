def printStr(n: int):
    if n == 0:
        print("Final Call")
        return
    
    print(n, "Days left!!")
    printStr(n - 1)

printStr(5)

# Print 1 to N
def uptoN(num: int, n: int):
    if num == n:
        print(num)
        return

    print(num)
    uptoN(num + 1, n)
print("Printing Numbers upto ", 10)
uptoN(1, 10)


# Print Even Numbers
def printEven(num: int):
    if num == 2:
        print(2)
        return

    if num % 2 == 0:
        printEven(num - 2)
    else:
        printEven(num - 1)

    print(num)

print("Printing Even Number!!!")
printEven(10)

# Factorial Number
def fact(num: int) -> int:
    if num <= 1:
        return 1

    return num * fact(num - 1)


print("Factorial", fact(10))

# Summo N numbers
# 6 -> 6 + 5 + 4 + 3 + 2 + 1
def sumo_num(n: int) -> int:
    if n == 1:
        return n

    return n + sumo_num(n - 1)

print("sumo_num", sumo_num(6))

# Power of 2
# 2^5 = 2 x 2 x 2 x 2 x 2 = 32
def power_of_two(num: int, n: int) -> int:
    if n == 1:
        return num

    return 2 * power_of_two(num, n - 1)

print("power_of_two of: ", power_of_two(2, 5))


def sum_sqr_num(n: int) -> int:
    """
    Sum square of N Number
    n = 4
    1^2 + 2^2 + 3^2 + 4^2 = 30
    TC - O(n), 
    SC - O(n) - becuase of stack

    | sum_sqr_num(4) |
    | sum_sqr_num(3) |
    | sum_sqr_num(2) |
    | sum_sqr_num(1) |
    |________________|  S T A C K (FILO)
    """

    if n <= 1:
        return n

    return n * n + sum_sqr_num(n - 1)

print("sum square of: ", sum_sqr_num(4))


def fibo(n: int) -> int:
    """
    fibonacci series
    0 1 1 2 3 5 8 13 21 34 55
    TC - O(2^n)
    SC - O(n) - recursion stack
    """

    if n <= 1:
        return n

    return fibo(n - 1) + fibo(n - 2)

print("fibo: ", fibo(10))

def fibo2(n: int, memo = {}) -> int:
    """
    This Time Complexity become O(n) because of memo (memorization)
    TC - O(n), SC - O(n)
    """

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibo2(n - 1) + fibo2(n - 2)
    return memo[n]

print("SC fibo2 ", fibo2(10))

# This solution will time exceed for greater than 43
def total_ways(n: int) -> int:
    """
    LC: 70 (easy)
    Nth stair n=5
    setps - 1, 2
    n = 0  n = 1  n = 2   n = 3      n = 4
      1     1      1+1    1+1+1      1+1+1,
                          1+2, 2+1   1+1+2, 1+2+1,
                                     2+1+1, 2+2
      1      1      2     1+2 = 3    2+3 = 5

    | Method           | Time Complexity |
    | ---------------- | --------------- |
    | Normal recursion | O(2ⁿ)           |
    | Memoization      | O(n)            |

    """

    if n <= 1:
        return 1
    
    return total_ways(n - 1) + total_ways(n - 2)
n = 44
# print("total_ways: " + str(n) + " is:", total_ways(n))

# in above solution what we do we use memorization to reduce TC [WORK IN LC]
def total_ways_memo(n: int, memo = None) -> int:
    """
    | Metric           | Value |
    | ---------------- | ------|
    | Time Complexity  | O(n)  |
    | Space Complexity | O(n)  |

    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    
    if n <= 1:
        return 1

    memo[n] = total_ways_memo(n - 1, memo) + total_ways_memo(n - 2, memo)

    return memo[n]

print("total_ways_memo with Memo: " + str(n) + " is:", total_ways_memo(n))

def gcd_two_num(a: int, b: int) -> int:
    """
    Greatest Common Divisior of two Number
    a = 18, b = 48
    ans. 6
    """
    if b == 0:
        return a

    return gcd_two_num(b, a % b)

print("GDC of:", gcd_two_num(18, 48))

# Recursion Array Problems:
print("---------------------")
print("Recusion in Array")
print("---------------------")

def print_arr(arr: list, index: int):
    """
    Print Array [2,3,4,6] -> 2 3 4 6
    """

    if index == 0:
        print(arr[index])
        return
    
    print_arr(arr, index - 1)
    print(arr[index])

arr = [1,2,3,4]
print_arr(arr, len(arr) - 1)

def sum_all_elem(arr: list, index: int) -> int:
    """
    array = [1, 2, 3, 4] 
    ans. - 1 + 2 + 3 + 4 = 10
    """
    if index == 0:
        return arr[index]
    
    return arr[index] + sum_all_elem(arr, index - 1)

print("sum_all_elem " + str(arr) + " is", sum_all_elem(arr, len(arr) - 1))

def find_min_elem(arr: list, index: int) -> int:
    """
    7 2 4 1 6 - 
    7, 2 => 2  2, 4 => 2  2, 1 => 1  1, 6 => 1
    ans => 1
    """
    if index == 0:
        return arr[index]
    
    return min(arr[index], find_min_elem(arr, index - 1))

arr2 = [2, 10 ,15, 19, 9]
print("find_min_elem" + str(arr2) + "=>", find_min_elem(arr2, len(arr2) - 1))

# Recusion in String
print("---------------------")
print("Recusion in String")
print("---------------------")

def check_palindrone(s: str, start: int, end: int) -> bool:
    """
    naman - True, MOM - True
    rohit - False
    we are consider input string is always in same case Lower or Upper (Not Mix)
    """
    # base cond.
    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return check_palindrone(s, start + 1, end - 1)

s = "naman"
print("check_palindrone", check_palindrone(s, 0, len(s) - 1))