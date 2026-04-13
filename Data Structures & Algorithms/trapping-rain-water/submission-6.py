class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        
        for i, n in enumerate(height):
            if (i != 0):
                max_left = max(height[0:i])
                max_right = max(height[i:len(height)])
                water += max(0, min(max_left, max_right) - n)
        return water

            
            
            


        