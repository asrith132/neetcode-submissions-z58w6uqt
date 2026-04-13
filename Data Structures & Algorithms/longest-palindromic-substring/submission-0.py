class Solution:
    def isPalindrome(self, s: str) -> int:
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if s[p1] != s[p2]:
                return -1
            p1 += 1
            p2 -= 1
        return len(s)
    
    def longestPalindrome(self, s: str) -> str:
        hashmap = {}
        max_len = 0
        res = ""
        for i in range(0, len(s)):
            for j in range(i, len(s) + 1):
                current_string = s[i:j]
                val = self.isPalindrome(current_string)
                if val > max_len:
                    res = current_string
                    max_len = val
        return res

            
        