class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)
        else:
            if num < (self.min_heap[0]):
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

        mlen = len(self.min_heap)
        maxlen = len(self.max_heap)
        while abs(mlen - maxlen) > 1:
            if len(self.min_heap) > len(self.max_heap):
                new_num = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -new_num)
                maxlen += 1
                mlen -= 1
            else:
                new_num = heapq.heappop(self.max_heap) * -1
                heapq.heappush(self.min_heap, new_num)
                maxlen -= 1
                mlen += 1


    def findMedian(self) -> float:
        if len(self.min_heap) == 0:
            mval = 0
        else:
            mval = self.min_heap[0]
        
        if len(self.max_heap) == 0:
            maxval = 0
        else:
            maxval = self.max_heap[0] * -1

        if abs(len(self.min_heap) - len(self.max_heap)) == 1:
            if len(self.min_heap) > len(self.max_heap):
                return mval
            else:
                return maxval
        else:
            return (mval + maxval) / 2

        
        