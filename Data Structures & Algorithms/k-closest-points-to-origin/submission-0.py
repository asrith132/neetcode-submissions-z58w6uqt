class Solution:
    import heapq

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x = point[0]
            y = point[1]
            distance = x ** 2 + y ** 2
            heapq.heappush(heap, (distance, point))
        
        res = []
        for i in range(0, k):
            dist, point = heapq.heappop(heap)
            res.append(point)
        return res
