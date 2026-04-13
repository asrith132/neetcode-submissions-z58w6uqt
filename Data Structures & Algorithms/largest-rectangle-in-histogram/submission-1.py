class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(0, len(heights)):
            height = heights[i]
            width = 1
            for j in range(i - 1, -1, -1):
                if height <= heights[j]:
                    width += 1
                else:
                    break
            for j in range(i + 1, len(heights)):
                if height <= heights[j]:
                    width += 1
                else:
                    break
            print()
            max_area = max(height * width, max_area)
        return max_area



        