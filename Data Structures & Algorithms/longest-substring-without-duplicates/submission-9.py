class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        i = 0
        maxcount = 0
        for j in range(len(s)):
            while s[j] in charset:
                charset.remove(s[i])
                i = i+1
            charset.add(s[j])
            maxcount = max(maxcount, len(charset))
        return maxcount
                