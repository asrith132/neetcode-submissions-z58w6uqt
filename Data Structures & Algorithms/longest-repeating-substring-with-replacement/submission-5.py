class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        r = 0
        res = 0
        for letter in s:
            count[ord(letter) - ord("A")] += 1
            length = r - l + 1
            if length - max(count) <= k:
                res = max(res, length)
            else:
                count[ord(s[l]) - ord("A")] -= 1
                l += 1
            r += 1
        return res

        
            
        