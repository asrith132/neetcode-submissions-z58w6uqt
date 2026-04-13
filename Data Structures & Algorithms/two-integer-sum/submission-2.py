class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            find = target - n
            if find in prevMap:
                return [prevMap[find], i]
            prevMap[n] = i;
        
        return False
