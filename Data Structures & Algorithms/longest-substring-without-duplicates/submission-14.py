class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 1
        max_length = 1
        string_length = len(s)
        if (string_length < 2):
            return string_length
        substring = s[p1:p2]
        while p2 < string_length: 
            if s[p2] not in substring:
                substring = s[p1:p2+1]
                max_length = max(max_length, len(substring))
                p2 += 1
            else:
                p1 += 1
                substring = s[p1:p2]
        return max_length
            
        
        