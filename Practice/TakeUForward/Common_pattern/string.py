# String Rotated by 2 Places
class Solution:
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
class Solution:
    def isRotated(self, s1, s2):
        if len(s1) != len(s2):
            return False

        # Clockwise rotation by 2
        clockwise = self.rotateClockwise(s1)
        if clockwise == s2:
            return True

        # Anti-clockwise rotation by 2
        anticlockwise = self.rotateAntiClockwise(s1)
        if anticlockwise == s2:
            return True

        return False

    def rotateClockwise(self, s):
        # Rotate last 2 chars to the front
        n = len(s)
        return s[-2:] + s[:-2]

    def rotateAntiClockwise(self, s):
        # Rotate first 2 chars to the end
        n = len(s)
        return s[2:] + s[:2]


# with simple 
class Solution:
    def isRotated(self, s1, s2):
        count1 = 0
        count2 = 0

        temp = s1

        # Rotate clockwise up to 2 times
        while count1 < 2:
            temp = self.rotateClockwise(temp)
            count1 += 1
            if temp == s2:
                return True

        temp = s1  # reset for anticlockwise

        # Rotate anti-clockwise up to 2 times
        while count2 < 2:
            temp = self.rotateAntiClockwise(temp)
            count2 += 1
            if temp == s2:
                return True

        return False

    def rotateClockwise(self, s):
        n = len(s)
        char = s[n - 1]
        new_str = char  # start with last character

        # copy remaining characters
        i = 0
        while i < n - 1:
            new_str += s[i]
            i += 1

        return new_str

    def rotateAntiClockwise(self, s):
        n = len(s)
        char = s[0]
        new_str = ""  # start empty

        # copy from index 1 to end
        i = 1
        while i < n:
            new_str += s[i]
            i += 1

        new_str += char  # add first character at end
        return new_str
