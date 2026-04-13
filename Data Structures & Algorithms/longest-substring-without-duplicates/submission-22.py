class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        p1 = 0
        p2 = 0
        max_len = 0 
        current = {}

        while p2 < len(s):
            if s[p2] in current:
                p1 = max(current[s[p2]] + 1, p1)
            current[s[p2]] = p2
            max_len = max(max_len, p2 - p1 + 1)
            p2 += 1
        return max_len


             