import math
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for char in s:
            if (char == "(" or char == "[" or char == "{"):
                my_stack.append(char)
            else:
                if my_stack:
                    val = my_stack[-1]
                    print(val)
                    if (char == ")" and val == "("):
                        my_stack.pop()
                    elif (char == "]" and val == "["):
                        my_stack.pop()
                    elif (char == "}" and val == "{"):
                        my_stack.pop()
                    else:
                        return False
                else:
                    return False
        if not bool(my_stack):
            return True
        return False
        

