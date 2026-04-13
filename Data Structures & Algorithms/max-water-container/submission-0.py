class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_count = 0
        while (i < j):
            count = (j - i) * min(heights[i], heights[j])
            if (count > max_count):
                max_count = count
            if (heights[i] > heights[j]):
                j = j - 1
            else:
                i = i + 1
        return max_count
        