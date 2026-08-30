class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []

        def dfs(curr, s, start):
            if s == target:
                res.append(curr.copy())
                return

            for i in range(start, len(nums)):
                if s + nums[i] <= target:
                    dfs(curr + [nums[i]], s + nums[i], i)

        dfs(arr, 0, 0)
        return res

