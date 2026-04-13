class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(0, len(heights)):
            height = heights[i]
            index = i
            while stack and stack[-1][1] >= height:
                top = stack.pop()
                width = i - top[0]
                max_area = max(top[1] * width, max_area)
                index = top[0]
            stack.append((index, height))
        while stack:
            top = stack.pop()
            width = len(heights) - top[0]
            print(f"max area = {top[1]} * {width}")
            max_area = max(top[1] * width, max_area)
        return max_area



        