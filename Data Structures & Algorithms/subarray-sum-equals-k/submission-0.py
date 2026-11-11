class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [2, 1, 2, 4]
        prefix_sum = [0] * len(nums)
        total = 0
        for i in range(0, len(nums)):
            total += nums[i]
            prefix_sum[i] = total
        
        
        hashmap = defaultdict(int)
        res = 0

        for i in range(0, len(prefix_sum)):
            current = prefix_sum[i]
            target = current - k
            if target == 0:
                res += 1
            res += hashmap[target]
            hashmap[current] += 1

        return res


        