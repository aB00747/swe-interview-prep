def spiralOrder(matrix):
    result = []
    top = 0
    left = 0
    bottom = len(matrix) - 1 # rows
    right = len(matrix[0]) - 1 # columns

    while top <= bottom and left <= right:
        # print columns forward
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        # print rows forward
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # print backward the rows
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        # print rows backward
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        
    return result

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print("spiralOrder", spiralOrder(matrix))


def transform(matrix):
    n = len(matrix)
    arr = []

    arr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            arr[j][i] = matrix[i][j]
        

    return arr


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print("transform", transform(matrix))

# in place tranform convert row to columns
def transformInPlace(matrix):
    n = len(matrix)
    tmp = 0
    left = 0

    for i in range(n):
        for j in range(i, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
        left += 1

    return matrix

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13, 14, 15, 16]]
# print(transformInPlace(matrix))


# Rotate Matrix by 90 degree clockwise (n x n)
def rotate90(martix):
    ans = []
    n = len(martix)

    ans = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ans[j][n - 1 - i] = matrix[i][j]

    return ans

matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
print("rotate 90", rotate90(matrix1))


# Leetcode -> LC.48 (Med.)
# Optimise space coplexity (in place) Rotate Matrix 90 degree
def OptimiseRotate90(matrix):
    n = len(matrix)

    # Tranpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # swape

    # Reverse
    for i in range(n):
        start = 0
        end = n - 1

        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1

    return matrix

matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
print("Optimise rotate 90 degree", OptimiseRotate90(matrix2))



def rotate180(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # swape


    # Reverse
    for i in range(n):
        start = 0
        end = n - 1

        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # swape


    # Reverse
    for i in range(n):
        start = 0
        end = n - 1

        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1

    return matrix

matrix3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
print("Rotate 180 -> ", rotate180(matrix3))


# different approach
def Optrotate180(matrix):
    n = len(matrix)
    ans = []


    for j in range(n):
        start = 0
        end = n - 1

        while start <= end:
            matrix[start][j], matrix[end][j] = matrix[end][j], matrix[start][j]
            start += 1
            end -= 1

    for i in range(n):
        start = 0
        end = n - 1

        while start <= end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1

    return matrix

matrix4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
print("Optrotate180", Optrotate180(matrix4))


# Rotate Matrix 90 degree anti-clockwiese
def antiRotate90(matrix):
    n = len(matrix)
    ans = [[0 for _ in range(n)] for _ in range(n)]
    
    # Tranpose
    for i in range(n):
        for j in range(n):
            ans[j][i] = matrix[i][j]

    # cloumn-wise reverse
    for j in range(n):
        start = 0
        end = n - 1

        while start <= end:
            ans[start][j], ans[end][j] = ans[end][j], ans[start][j]
            start += 1
            end -= 1


    return ans

matrix5 = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
print("antiRotate90", antiRotate90(matrix5))



# Rotate Matrix by k times
def rotateKtimes(k, matrix):
    k = k % 4

    while k > 0:
        matrix = OptimiseRotate90(matrix)

        k -= 1

    return matrix

print("rotateKtimes", rotateKtimes(99, matrix5))

# 74. Search a 2D Matrix
def searchMatrix(matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = n * m - 1

        while start <= end:
            mid = (start + end) // 2
            row_index = mid // n
            col_index = mid % n

            if matrix[row_index][col_index] == target:
                return True
            elif matrix[row_index][col_index] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False

# Search in a Row-Column Sorted
def matSearch(mat, x):
    n = len(mat)
    m = len(mat[0])
    # start from right to left 
    i = 0
    j = m - 1

    while i < n and j >= 0:
        if mat[i][j] == x:
            return True
        elif mat[i][j] < x:
            # move down for greater bcz value is smaller than target
            i += 1
        else:
            # move left for smaller bcz value is larger than target
            j -= 1

    return False

mat = [[3, 30, 38],[20, 52, 54],[35, 60, 69]]
x = 20
# 62
print(matSearch(mat, x))