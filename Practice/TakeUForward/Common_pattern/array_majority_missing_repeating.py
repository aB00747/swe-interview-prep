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



"""
>>> Boyer-Moore Voting Algorithm
LC: 169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.  
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
def majorityElement(nums):
    cand = 0
    count = 0
    n = len(nums)

    for i in range(n):
        if count == 0:
            count = 1
            cand = nums[i]
        else:
            if cand == nums[i]:
                count += 1
            else:
                count -= 1

    count2 = 0
    for i in range(n):
        if nums[i] == cand:
            count2 += 1

    if count2 > (n // 2):
        return cand
    else:
        return None

nums = [2,2,1,1,1,2,2] # o/p: 2
print("majorityElement", majorityElement(nums))