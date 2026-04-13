class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close_dict = {"{":"}", "(":")", "[":"]"}
        for letter in s:
            if letter == "{" or letter == "(" or letter == "[":
                stack.append(letter)
            else:
                if stack:
                    val = stack.pop()
                    if open_close_dict[val] != letter:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
        