# 22-04-2026

# amstrong numbers
def ams_num(num):
    if not num:
        return 0
    
    ams_sum = 0

    while num > 0:
        ld = num % 10
        ams_sum += pow(ld, 3)
        num //= 10

    return ams_sum

print(ams_num(371))


# With Recursion
# fibonacci series
def fib(n):
    if n <= 1:
        return 1
    
    return fib(n-1) + fib(n-2)

print(fib(4))

# Palidrome of string
# MADAM
def is_pali(s, n, i):
    if not s:
        return False
    
    if i >= n // 2:
        return True
    
    if s[i] != s[n - i - 1]:
        return False
    
    return is_pali(s, n, i + 1)

print(is_pali("MADAME", 5, 0))

# hashing count the number with O(1)
class CountNumber:
    def __init__(self) -> None:
        self.mpp = {}

    def store(self, arr: list) -> bool:
        if arr is None:
            return False
        

        for i in range(len(arr)):
            self.mpp[arr[i]] = self.mpp.get(arr[i], 0) + 1

        return True
    
    def get_count(self, val: int) -> int:
        if not val or val not in self.mpp:
            return 0
        
        return self.mpp[val]
    

obj = CountNumber()
obj.store([1, 2, 3, 1, 3, 2, 2, 12])
print(obj.get_count(3))

# Sorting Algo
# Selection Sort
# [3, 46, 24, 52, 20, 9] -> [3, 9, 20, 24, 46, 52]
def selection_sort(arr: list) -> list: 
    n = len(arr)
    # min_index = 0

    for i in range(n - 1):
        min_index = i

        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print("Selection Sort", selection_sort([3, 46, 24, 52, 20, 9]))


# Bubble sort
def bubble_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n -1, 0, -1):
        did_swap = False
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True
        
        if did_swap == False:
            break

        
    return arr

print("Bubble Sort", bubble_sort([3, 46, 24, 52, 20, 9]))

# Insertion Sort
def insertion_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
        
    return arr

print("Insertion Sort", insertion_sort([3, 46, 24, 52, 20, 9]))

# Merge Sort
def merge_sort(arr: list, low: int, high: int) -> None:
    if low >= high:
        return
    
    mid = low + (high - low) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    merge(arr, low, mid, high)


def merge(arr: list, low: int, mid: int, high: int) -> None:
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1


    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

un_sort = [3, 46, 24, 52, 20, 9]
merge_sort(un_sort, 0, len(un_sort) - 1)
print("merge_sort", un_sort)