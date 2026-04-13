class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        p1 = 0
        p2 = 0
        max_len = 0 
        current = set()
        while p2 < len(s):
            if s[p2] not in current:
                current.add(s[p2])
            else:
                while s[p2] in current:
                    current.remove(s[p1])
                    p1 += 1
                current.add(s[p2])
            max_len = max(max_len, len(current))
            p2 += 1
        return max_len


             