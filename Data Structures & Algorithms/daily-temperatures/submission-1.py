class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                val = stack.pop()
                temperatures[val] = i - val
            stack.append(i)
        for element in stack:
            temperatures[element] = 0
        return temperatures

        