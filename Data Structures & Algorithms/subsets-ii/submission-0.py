class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        curr = []
        nums.sort()

        def dfs(arr, start):
            res.append(arr.copy())
                
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                else:
                    dfs(arr + [nums[i]], i + 1)

        
        dfs(curr, 0)
        return res
