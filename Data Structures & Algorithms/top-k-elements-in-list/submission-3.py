class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        arr = [[] for i in range(len(nums) + 1)]
        for key, val in hashmap.items():
            arr[val].append(key)
        
        res = []
        current = len(nums)
        while k > 0:
            if arr[current] != []:
                res.append(arr[current].pop()) 
                k -= 1
            else:
                current -= 1
        return res
