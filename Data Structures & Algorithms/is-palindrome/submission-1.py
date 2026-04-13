import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if (c.isalnum()):
                newStr += c.lower()
        print(newStr)
        for i in range(0, math.floor((len(newStr)/2))):
            if (newStr[i] != newStr[-i + -1]):
                return False
        return True
        