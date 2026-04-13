import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for item in stones:
            heapq.heappush(heap, -item)
        
        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            if s1 != s2:
                heapq.heappush(heap, -abs(s1 - s2))
        if heap:
            return -heap[0]
        else:
            return 0

