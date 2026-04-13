class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        p1 = 0
        p2 = 0
        max_len = 0 
        while p1 < len(s):
            current = set()
            while p2 < len(s):
                if s[p2] not in current:
                    current.add(s[p2])
                else:
                    break
                p2 += 1
            max_len = max(max_len, len(current))
            p1 += 1
            p2 = p1
        return max_len


             