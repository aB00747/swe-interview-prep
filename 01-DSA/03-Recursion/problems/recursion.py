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
# 2^5 = 2 x 2 x 2 x 2 x 2
def power_of_two(n: int) -> int:
    if n == 1:
        return 2
    
    return 2 * power_of_two(n - 1)

print(power_of_two(5))