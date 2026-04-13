class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        count = [0] * 26
        for letter in s1:
            count[ord(letter) - ord("a")] += 1
        l = 0
        r = len(s1)
        while r <= len(s2):
            check_count = [0] * 26
            for i in range(l, r):
                check_count[ord(s2[i]) - ord("a")] += 1
            if (count == check_count):
                return True
            l += 1
            r += 1
        
        return False
            

        