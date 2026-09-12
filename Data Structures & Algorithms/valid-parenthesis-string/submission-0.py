class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, val in enumerate(s):
            if val == "(":
                left.append(i)
            elif val == "*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while left and star:
            if left.pop() < star.pop():
                continue
            else:
                return False
            
        return not left