class Solution:
    def expand(self, p1, p2, s) -> str:
        string = ""
        while p1 >= 0 and p2 < len(s):
            if s[p1] == s[p2]:
                string = s[p1:p2+1]
            else:
                break
            p1 -= 1
            p2 += 1
        return string
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return
        max_string = s[0]
        for i in range(0, len(s)):
            center = i
            p1 = center - 1
            p2 = center + 1
            string_one = self.expand(p1, p2, s)
            
            p1 = center
            p2 = center + 1
            string_two = self.expand(p1, p2, s)
            if len(string_one) > len(max_string):
                max_string = string_one
            if len(string_two) > len(max_string):
                max_string = string_two

        return max_string
                    
                    


            
        

            
        