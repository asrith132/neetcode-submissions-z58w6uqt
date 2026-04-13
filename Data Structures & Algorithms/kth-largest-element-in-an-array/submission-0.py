class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(0, len(nums)):
            if i < k:
                heapq.heappush(heap, nums[i])
            else:
                heapq.heappush(heap, nums[i])
                heapq.heappop(heap)
        return heap[0]
        