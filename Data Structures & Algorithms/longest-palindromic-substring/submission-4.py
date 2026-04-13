class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_string = ""
        for i in range(0, len(s)):
            center = i
            p1 = center - 1
            p2 = center + 1
            current_string = s[center]
            while p1 >= 0 and p2 < len(s):
                if s[p1] == s[p2]:
                    current_string = s[p1:p2+1]
                else:
                    break
                p1 -= 1
                p2 += 1
            if len(current_string) > len(max_string):
                max_string = current_string
            
            p1 = center
            p2 = center + 1
            while p1 >= 0 and p2 < len(s):
                if s[p1] == s[p2]:
                    current_string = s[p1:p2+1]
                else:
                    break
                p1 -= 1
                p2 += 1
            if len(current_string) > len(max_string):
                max_string = current_string
        return max_string
                    
                    


            
        

            
        