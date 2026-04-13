class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temp_len = len(temperatures)
        res = [0] * temp_len
        for i in range(0, temp_len):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                val = stack.pop()
                res[val] = i - val
            stack.append(i)
        return res

        