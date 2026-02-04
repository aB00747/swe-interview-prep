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