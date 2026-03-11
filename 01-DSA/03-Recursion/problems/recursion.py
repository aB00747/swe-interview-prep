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
def sum_sqr_num(n: int) -> int:
    if n <= 1:
        return n

    return n * n + sum_sqr_num(n - 1)

print("sum square of: ", sum_sqr_num(4))

"""
fibonacci series
0 1 1 2 3 5 8 13 21 34 55
TC - O(2^n)
SC - O(n) - recursion stack
"""
def fibo(n: int) -> int:
    if n <= 1:
        return n

    return fibo(n - 1) + fibo(n - 2)

print("fibo: ", fibo(10))

"""
This Time Complexity become O(n) because of memo (memorization)
TC - O(n), SC - O(n)
"""
def fibo2(n: int, memo = {}) -> int:
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibo2(n - 1) + fibo2(n - 2)
    return memo[n]

print("SC fibo2 ", fibo2(10))
