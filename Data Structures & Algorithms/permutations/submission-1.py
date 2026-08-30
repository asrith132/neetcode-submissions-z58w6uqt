class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        arr = []
        choices = [False] * len(nums)

        def dfs(arr, choices):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for i in range(0, len(choices)):
                if choices[i] == False:
                    choices[i] = True
                    dfs(arr + [nums[i]], choices)
                    choices[i] = False

        dfs(arr, choices)
        return res
