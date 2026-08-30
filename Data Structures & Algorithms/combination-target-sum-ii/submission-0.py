class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()

        def dfs(arr, s, start):
            if s == target:
                res.append(arr.copy())
                return
            
            for i in range(start, len(candidates)):
                if s + candidates[i] <= target:
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    else:
                        dfs(arr + [candidates[i]], s + candidates[i], i + 1)



        dfs(curr, 0, 0)
        return res

