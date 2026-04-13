class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"{":"}", "(":")", "[":"]"}
        for char in s:
            if char == "{" or char == "[" or char == "(":
                stack.append(char)
            else:
                if not stack or char != dic[stack.pop()]:
                    return False
        return not stack
            
                
        


