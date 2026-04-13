class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        count = [0] * 26
        max_length = 0
        for letter in s:
            count[ord(letter) - ord("A")] += 1
            length = r - l + 1
            if length - max(count) <= k:
                max_length = max(length, max_length)
            else:
                count[ord(s[l]) - ord("A")] -= 1
                l += 1
            r += 1
        return max_length


            