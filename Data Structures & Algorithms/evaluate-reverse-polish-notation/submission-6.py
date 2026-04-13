import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        if (len(tokens) == 1):
            print(len(tokens))
            return int(tokens[0])
        for t in tokens:
            pop = t
            if (pop == "+"):
                val_one = stack.pop()
                val_two = stack.pop()
                stack.append(int(val_two) + int(val_one))
            elif (pop == "*"):
                val_one = stack.pop()
                val_two = stack.pop()
                stack.append(int(val_two) * int(val_one))
            elif (pop == "-"):
                val_one = stack.pop()
                val_two = stack.pop()
                stack.append(int(val_two) - int(val_one))
            elif (pop == "/"):
                val_one = stack.pop()
                val_two = stack.pop()
                if (math.floor(int(val_two) / int(val_one)) < 0):
                    stack.append(math.floor(int(val_two) / int(val_one) * -1) * -1)
                else:
                    stack.append(math.floor(int(val_two) / int(val_one)))
            else:
                stack.append(t)
        return stack[0]