"""
Docstring for Common_pattern.array_majority_missing_repeating
Missing And Repeating
GFG: https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
Input: arr[] = [2, 2]
Output: [2, 1]
Explanation: Repeating number is 2 and the missing number is 1.
"""
def findTwoElement(arr):
    n = len(arr)
    res = [0, 0]

    for i in range(n):
        arr[i] -= 1

    for i in range(n):
        arr[arr[i] % n] += n
    
    for i in range(n):
        # occurence
        if arr[i] // n == 2:
            res[0] = i + 1
        elif arr[i] // n == 0:
            res[1] = i + 1
    
    return res

arr = [2, 2]
print("findTwoElement", findTwoElement(arr))
