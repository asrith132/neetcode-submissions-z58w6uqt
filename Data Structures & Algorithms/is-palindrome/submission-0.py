class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pointer_one = 0
        pointer_two = len(s) - 1
        while (pointer_one < pointer_two):
            if (s[pointer_one].isalnum() == True):
                if (s[pointer_two].isalnum() == True):
                    if (s[pointer_one] != s[pointer_two]):
                        return False
                    else:
                        pointer_one += 1
                        pointer_two -= 1
                else:
                    pointer_two = pointer_two - 1
            else:
                pointer_one = pointer_one + 1
        return True
                