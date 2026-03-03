# find the longest subarry with sum of k 
arr = [2, 5, 1, 7 , 10]
k = 14

def longest_subarray(arr, k):
    l = r = 0
    curr_sum = 0
    max_len = 0
    n = len(arr)

    while r < n:
        curr_sum += arr[r]

        if curr_sum > k:
            curr_sum -= arr[l]
            l += 1

        if curr_sum <= k:
            max_len = max(max_len, r - l + 1)


        r += 1

    return max_len


print(longest_subarray(arr, k))


# Maximum points you can obtain from cards
# arr = [6, 2, 3, 4, 7, 2, 1, 7, 1]
def max_card(arr, k):
    n = len(arr)
    l = k - 1
    r = n - 1
    curr_sum = sum(arr[:k])
    max_sum = curr_sum

    while l >= 0:
        curr_sum -= arr[l]
        l -= 1

        curr_sum += arr[r]
        r -= 1

        max_sum = max(max_sum, curr_sum)

    return max_sum

arr1 = [6, 2, 3, 4, 7, 2, 1, 7, 1]
print(max_card(arr1, 4))


# longest non repeative character string

def longest_string(s):
    n = len(s)
    max_len = 0

    for i in range(n):
        hashing = {}

        for j in range(n):
            if hashing.get(s[j]) == 1:
                break
            
            max_len = max(max_len, j - i + 1)
            hashing[s[j]] = 1

    return max_len


print(longest_string("cadbzabcd"))


def longest_unique_string_window(str):
    l = r = 0
    max_len = 0
    n = len(str)
    hash_map = {}

    while r < n:
        hash_map[str[r]] = hash_map.get(str[r], 0) + 1

        while hash_map.get(str[r]) > 1:
            # hash_map[str[l]] -= 1
            hash_map[str[l]] -= 1
            l += 1

        max_len = max(max_len, r - l + 1)

        r += 1

    return max_len

print(longest_unique_string_window("cadbzabcd"))


def max_conse_ones(arr, k):
    l = r = 0
    max_len = 0
    count = 0
    n = len(arr)

    while r < n:
        if arr[r] == 0:
            count += 1

        if count > k:
            if arr[l] == 0:
                count -= 1
            l += 1

        if count <= k:
            max_len = max(max_len, r - l + 1)

        r += 1

    return max_len

print("max_conse_ones", max_conse_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))


# constant window
# array size is 6 -> n - 1
# [1, 2, 3 , 4, 5, 6]
# find the max sum with window size 3
def constWindow(arr, k):
    l = 0
    n = len(arr)
    r = k - 1
    max_sum = 0
    curr_sum = 0

    # for i in range(k):
    #     curr_sum += arr[i]
    curr_sum = sum(arr[:k])
    max_sum = curr_sum

    while(r < n):
        curr_sum += arr[r]
        r += 1

        curr_sum -= arr[l]
        l += 1

        max_sum = max(max_sum, curr_sum)

    return max_sum


arr = [1, 2, 3 , 4, 5, 6]
print("constWindow", constWindow(arr, 3))

"""
2. First Negative Number in Every Window of Size K
➤ For each window, find the first negative number (or 0 if none).
"""
#   0   1   2   3   4   5   6   7
# [12, -1, -7, 8, -15, 30, 16, 28]
# o/p: [-1, -1, -7, -15, -15, 0]
#   ^       ^
# r++, l++
# r will scan and try to find -ve value
# l will check if it remove or not the  only it allow to add new -ve value
# one variable to store the tmp -ve value


def firstNegative(arr, k):
    l = r = 0
    n = len(arr)
    tmp = 0
    res = []

    while l <= r and r < n:
        if r - l + 1 == k:
            found = 0
            for i in range(l, r):
                if (arr[i] < 0):
                    found = arr[i]
                    break
            res.append(found)
            l += 1
        r += 1
    return res

arr2 = [12, -1, -7, 8, -15, 30, 16, 28]

print("firstNegative", firstNegative(arr2, 3))

"""
Count Occurrences of Anagrams
➤ Count how many substrings of length len(p) in string s are anagrams of p.
s = "forxxorfxdofr"
     ^ ^
p = "for"
> 3

"for" → f:1, o:1, r:1
"orf" → f:1, o:1, r:1  ✅ same

"""

# save store in hash p with value:freq
# length of p will be the window
# if char curr_freq > expect_freq will move pointer (decrease order) until match the expect_freq

def countOccuur(str, exp_str):
    n = len(str) 
    # window size
    k = len(exp_str)
    result = {}
    hash = {}
    l = r = 0
    count = 0


    for i in range(k):
        result[exp_str[i]] = result.get(exp_str[i], 0) + 1
    
    while r < n:
        hash[str[r]] = hash.get(str[r], 0) + 1

        # shrink and del if zero freq char
        while r - l + 1 > k:
            hash[str[l]] -= 1
            if (hash[str[l]]) == 0:
                del hash[str[l]]
            l += 1
        
        if r - l + 1 == k and  hash == result:
            count += 1

        r += 1

    return count

# s = "forxxorfxdofr"
s = "xyzajjasjjdajsdak"
p = "for"
print(countOccuur(s, p))

# print(chr(97)) convert ASCII to character
# print(ord('a')) char to ASCII

# selection sort
def selSort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i, n):
            # find minimal
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr

arr4 = [13, 46, 52, 20 , 9]
# print(selSort(arr4))

# Bubble sort
def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1, -1):
        for j in range(n):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(bubbleSort(arr4))