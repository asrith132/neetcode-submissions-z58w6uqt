import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                vone = int(stack.pop())
                vtwo = int(stack.pop())
                print(f"{vtwo} + {vone}")
                stack.append(vtwo + vone)
            elif t == "*":
                vone = int(stack.pop())
                vtwo = int(stack.pop())
                print(f"{vtwo} * {vone}")
                stack.append(int(vtwo) * int(vone))
            elif t == "-":
                vone = int(stack.pop())
                vtwo = int(stack.pop())
                print(f"{vtwo} - {vone}")
                stack.append(vtwo - vone)
            elif t == "/":
                vone = int(stack.pop())
                vtwo = int(stack.pop())
                if vtwo / vone < 0:
                    val = math.floor(vtwo / vone * -1) * -1
                else:
                    val = math.floor(vtwo / vone)
                print(f"{vtwo} / {vone}")
                stack.append(val)
            else:
                stack.append(t)
        return int(stack[-1])
            