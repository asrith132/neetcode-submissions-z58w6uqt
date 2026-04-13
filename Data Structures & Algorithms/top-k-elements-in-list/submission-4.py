class Solution:
    import heapq 

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

        heap = []
        for key, val in hashmap.items():
            heapq.heappush(heap, (-1 * val, key))
        res = []
        for i in range(0, k):
            val, key = heapq.heappop(heap)
            res.append(key)

        return res

        