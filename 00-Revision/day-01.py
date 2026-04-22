# Two Sum II
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given a sorted array of distinct integers and an integer representing a target sum,
    returns indices of the two numbers such that they add up to the target sum.
    
    The function takes advantage of the fact that the input array is sorted and uses
    the two-pointer technique to find the solution in O(n) time complexity.

    Args:
        nums (list[int]): A sorted array of distinct integers.
        target (int): An integer representing the target sum.

    Returns:
        list[int]: Indices of the two numbers such that they add up to the target sum.
    """
    i = 0
    j = len(nums) - 1
    curr = 0

    while i < j:
        curr = nums[j] + nums[i]

        if curr == target:
            return [i + 1, j + 1]
        
        if curr < target:
            i += 1
        else:
            j -= 1

    return []

test_cases = [([2,7,11,15], 9), ([-1,0], -1), ([2,3,4], 6)]
for nums, target in test_cases:
    print("Two Sum II", two_sum(nums, target))

# Container With Most Water
def max_water(arr: list) -> int:
    """
    Calculate the maximum area of water that can be trapped between bars
    represented by the input array.

    Parameters
    ----------
    arr : list
        Input array

    Returns
    -------
    int
        Maximum area of water that can be trapped
    """
    i = 0
    j = len(arr) - 1
    max_area = 0

    while i < j:
        # Area = width x Height
        area = (j - i) * min(arr[i], arr[j])
        # max area
        max_area = max(max_area, area)
        # i is lesser then move i forward because we want max
        # or else move j to find max height
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1

    return max_area

# arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]

test_cases_water = [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)]
for arr, output in test_cases_water:
    print("max_water", max_water(arr), "PASSED:", max_water(arr) == output)


# Valid Palindrome string
def isPalidrome(s: str) -> bool:
    """
    Returns True if the given string is a valid palindrome and False otherwise.

    A valid palindrome is a string that reads the same backwards as forwards, ignoring
    case and non-alphanumeric characters.

    Parameters
    ----------
    s : str
        Input string

    Returns
    -------
    bool
        True if the given string is a valid palindrome, False otherwise
    """
    lower = s.lower()
    result = ""
    
    # for char in lower:
    #     if char.isalnum():
    #         result += char
    result = "".join([char for char in lower if char.isalnum()])

    for i in range(len(result) // 2):
        if result[i] != result[len(result) - 1 - i]:
            return False
        
    return True


# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

test_cases_pal = [("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)]
for string, output in test_cases_pal:
    print("Valid Palindrome string", isPalidrome(string), "PASSED:", isPalidrome(string) == output)


"""
Date: 06-04-2026; Day: Monday

Today I learned:
- Two Sum II (LC 167)
- Container With Most Water (LC 11)
- Valid Palindrome (LC 125)

Completed Two pointer easy problems of Leetcode

"""