# String Rotated by 2 Places
def isRotated(self,s1,s2):
    count1 = 0
    count2 = 0
    s1_list = list(s1)
    
    while count1 < 2:
        s1_list = self.rotateClockwise(s1_list)
        count1 += 1

        if ''.join(s1_list) == s2:
            return True
            
    s1_list = list(s1)
    
    while count2 < 2:
        s1_list = self.rotateAntiClockwise(s1_list)
        count2 += 1
    
        if ''.join(s1_list) == s2:
            return True
        
    return False


def rotateClockwise(self, s):
    n = len(s)
    char = s[n - 1]
    index = n - 1
    
    while index > 0:
        # s[index + 1] = s[index]
        s[index] = s[index - 1]
        index -= 1
        
    s[0] = char
    
    return s
    
def rotateAntiClockwise(self, s):
    n = len(s)
    char = s[0]
    index = 0
    
    while index < n - 1:
        # s[index - 1] = s[index]
        s[index] = s[index + 1]
        index += 1
        
    s[n - 1] = char
    
    return s

# with slicing
# def isRotated(self, s1, s2):
#     if len(s1) != len(s2):
#         return False

#     # Clockwise rotation by 2
#     clockwise = self.rotateClockwise(s1)
#     if clockwise == s2:
#         return True

#     # Anti-clockwise rotation by 2
#     anticlockwise = self.rotateAntiClockwise(s1)
#     if anticlockwise == s2:
#         return True

#     return False

# def rotateClockwise(self, s):
#     # Rotate last 2 chars to the front
#     n = len(s)
#     return s[-2:] + s[:-2]

# def rotateAntiClockwise(self, s):
#     # Rotate first 2 chars to the end
#     n = len(s)
#     return s[2:] + s[:2]


# with simple 
# def isRotated(self, s1, s2):
#     count1 = 0
#     count2 = 0

#     temp = s1

#     # Rotate clockwise up to 2 times
#     while count1 < 2:
#         temp = self.rotateClockwise(temp)
#         count1 += 1
#         if temp == s2:
#             return True

#     temp = s1  # reset for anticlockwise

#     # Rotate anti-clockwise up to 2 times
#     while count2 < 2:
#         temp = self.rotateAntiClockwise(temp)
#         count2 += 1
#         if temp == s2:
#             return True

#     return False

# def rotateClockwise(self, s):
#     n = len(s)
#     char = s[n - 1]
#     new_str = char  # start with last character

#     # copy remaining characters
#     i = 0
#     while i < n - 1:
#         new_str += s[i]
#         i += 1

#     return new_str

# def rotateAntiClockwise(self, s):
#     n = len(s)
#     char = s[0]
#     new_str = ""  # start empty

#     # copy from index 1 to end
#     i = 1
#     while i < n:
#         new_str += s[i]
#         i += 1

#     new_str += char  # add first character at end
#     return new_str

# LC:1108. Defanging an IP Address
def defangIPaddr(address: str) -> str:
    arr = list(address)
    n = len(arr)
    ans = ''

    for i in range(n):
        if arr[i] == '.':
            ans += '[.]'
        else:
            ans += arr[i]

    return ans

address = "1.1.1.1"
print(defangIPaddr(address))

# LC:1832. Check if the Sentence Is Pangram
def checkIfPangram(sentence: str) -> bool:
        hashing = {}
        # hashing = [0] * 26
        n = len(sentence)

        for i in range(n):
            index = ord(sentence[i]) - ord('a')
            hashing[index] = 1

        for i in range(26):
            if hashing.get(i, 0) == 0:
            # if hashing[i] == 0:
                return False

        return True

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))

# Sort String
# s = edcab -> abcde
# def sortStr(string: str) ->str:


# LC:409. Longest Palindrome
def longestPalindrome(s: str) -> int:
    n = len(s)
    upper = [0] * 26
    lower = [0] * 26
    odd = 0
    count = 0

    for i in range(n):
        if ord(s[i]) >= ord('a'):
            lower[ord(s[i]) - ord('a')] += 1
        else:
            upper[ord(s[i]) - ord('A')] += 1

    for i in range(26):
        if lower[i] % 2 == 0:
            # even
            count += lower[i]
        else:
            # odd
            count += lower[i] - 1
            odd = 1

        if upper[i] % 2 == 0:
            count += upper[i]
        else:
            count += upper[i] - 1
            odd = 1

    return count + odd

# s = "abccccdd"
# s = "ccc"
s = "abccccdd"
print(longestPalindrome(s))

# KMP what will longest prefix and suffix
def longPrefixSuffix(string):
    print("calling you")
    n = len(string)
    prefix = ''
    sufix = ''
    max_len = 0

    for i in range(n - 1):
        prefix = string[:i]
        sufix = string[n - i:]


        print("prefix", prefix)
        print("sufix", sufix)

        if prefix == sufix:
            max_len = max(max_len, len(prefix))


    return max_len

# ex_string = "ABCDEABCD"
ex_string = "ABCDEAFCD"
print("longPrefixSuffix 1", longPrefixSuffix(ex_string))


def longPrefixSuffix2(string):
    n = len(string)
    max_len = 0

    for l in range(1, n):  # check lengths 1..n-1
        match = True
        for i in range(l):
            print("prefix", string[i])
            print("sufix", string[n - l + i])
            print("length", l)
            if string[i] != string[n - l + i]:
                match = False
                break
        if match:
            max_len = l

    return max_len


print("longPrefixSuffix 2:", longPrefixSuffix2(ex_string))
