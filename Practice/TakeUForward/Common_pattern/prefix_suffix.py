# Max Difference between 2 elements

def test_max_diff(arr):
    n = len(arr)
    if n < 2:
        return 0

    ans = float('-inf')

    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, abs(arr[j] - arr[i]))

    return ans


elem1 = [9, 5, 8, 12, 2, 3, 7, 4]
print(test_max_diff(elem1))

def max_diff(arr):
    n = len(arr)
    suff = 0
    diff = 0

    for i in range(n - 1, -1, -1):
        suff = max(suff, arr[i])

        diff = max(diff, abs(suff - arr[i]))

    return diff

elem = [9, 5, 8, 12, 2, 3, 7, 4]
print(max_diff(elem))