class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 1):
            return 1
        i = 0
        j = 0
        max_count = 0
        count = 0
        for i in range(len(s) - 1):
            while(len(set(s[i:j])) == len(s[i:j])):
                j += 1
                if (j > len(s) - 1):
                    break
            if (j > len(s) - 1):
                break
            count = j - i - 1
            max_count = max(max_count, count)
        if(len(set(s[i:j])) == len(s[i:j])):
            count = j - i
        else:
            count = j - i - 1
        max_count = max(max_count, count)
        return max_count
                