class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        hashmap = {}
        res = 0
        for i in range(0, len(nums)):
            val = nums[i]
            hashmap[val] = max(hashmap.get(val, 0), hashmap.get(k, 0)) + 1
            res = max(res, hashmap[val] - hashmap.get(k, 0))
        return res + hashmap.get(k, 0)
            
            

            

        
