"""
🎯 ROUND 1 — Coding + Problem Solving
Question 1: (Medium – Very Common Pattern)

Problem:
Given an array of integers nums and an integer k, return the maximum sum of any subarray of size k.
nums = [2, 1, 5, 1, 3, 2]
k = 3
Output: 9   // subarray [5,1,3]
"""
def max_sub(nums, k):
    if len(nums) < k:
        return 0

    i = curr_sum = max_sum = 0

    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    j = k 

    while j < len(nums):
        curr_sum += nums[j]

        if j - i + 1 > k:
            curr_sum -= nums[i]
            i += 1

        max_sum = max(max_sum, curr_sum)
        j += 1

    return max_sum

print(max_sub([2, 1, 5, 1, 3, 2], 3))

# with using pre-defined function
def max_sum1(nums, k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum

    for i in range(k, len(nums)):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]
        max_sum = max(max_sum, curr_sum)

    return max_sum

print(max_sum1([2, 1, 5, 1, 3, 2], 3))

"""
👉 What if I change the question:

“Find the maximum sum subarray of any size (not fixed k)”

What will you do?
> This become Kandane's Algo
nums = [2, -1, 5, -3, 4]
o/p = 6
"""
def max_subarr(nums):
    if len(nums) == 0:
        return 0

    max_sum = 0
    prefix = 0

    for i in range(len(nums)):
        prefix += nums[i]

        max_sum = max(max_sum, prefix)

        if prefix < 0:
            prefix = 0

    return max_sum

print(max_subarr([2, -1, 5, -3, 4]))

"""
🎯 ROUND 2 — Data Structures (Important)
Question 2:

Design a data structure that supports:

insert(val)
remove(val)
getRandom()

All in O(1) time.

e.g. 
insert(1)
insert(2)
remove(1)
getRandom() → 2
"""
import random

class RandomSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val):
        if val in self.map:
            return False

        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val):
        if val not in self.map:
            return False
        
        index = self.map[val]
        last_val = self.arr[-1]

        # swap
        self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]

        # update move element index
        self.map[last_val] = index

        self.arr.pop()
        del self.map[val]

        return True

    def get_random(self):
        if not self.arr:
            return None

        return random.choice(self.arr)

    def get_val(self):
        print("Array")
        print(self.arr)
        print("MAP")
        print(self.map)

obj = RandomSet()
obj.insert(10)
obj.insert(30)
obj.insert(40)
obj.get_val()
obj.remove(40)
obj.get_val()

print(obj.get_random())

"""
🎯 ROUND 3 — HARDER (Google-style thinking)
Question 3: (Very Important Pattern)

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: 3  // "abc"
"""
def longest_substr(s):
    if not s:
        return 0
    
    i = j = max_len = 0
    n = len(s)
    mapp = {}

    for  j in range(n):
        mapp[s[j]] = mapp.get(s[j], 0) + 1

        while mapp[s[j]] > 1:
            mapp[s[i]] -= 1
            i += 1

        max_len = max(max_len, j - i + 1)

    return max_len

# print(longest_substr("abcabcbb"))
print(longest_substr("pwwkew"))


"""
🚀 ROUND 4 — Graph + BFS (Google Favorite)
Question 6:

You are given a binary grid (0 = water, 1 = land).
Find the number of islands.

Example:
grid = [
  ["1","1","0","0"],
  ["1","1","0","0"],
  ["0","0","1","0"],
  ["0","0","0","1"]
]

Output: 3
"""