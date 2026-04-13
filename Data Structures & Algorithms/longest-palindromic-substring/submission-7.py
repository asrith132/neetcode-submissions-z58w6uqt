class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_string = ""

        for letter in range(0, len(s)):
            even_center = letter
            p1 = even_center
            p2 = even_center
            current_string = ""
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                current_string = s[p1: p2 + 1]
                p1 -= 1
                p2 += 1
            if len(max_string) < len(current_string):
                max_string = current_string

            odd_center = letter
            p1 = odd_center
            p2 = odd_center + 1
            current_string = ""
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                current_string = s[p1: p2 + 1]
                p1 -= 1
                p2 += 1
            if len(max_string) < len(current_string):
                max_string = current_string
            
        return max_string

            
                    


            
        

            
        