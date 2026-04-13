class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        res = 0
        for i in range(0, len(nums)):
            val = nums[i]
            hashmap[val] = max(hashmap[val], hashmap[k]) + 1
            res = max(res, hashmap[val] - hashmap[k])
        return res + hashmap[k]
            
            

            

        
