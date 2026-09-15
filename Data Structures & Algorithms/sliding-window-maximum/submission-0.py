class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #have a max heap strucutre w k elements in it
        #have a expiry time for each element in the heap if the expiry team happened then its not valid for the window we are using
        #append elements into the heap as we add items into the window

        max_heap = []
        for i in range(0, k - 1):
            heapq.heappush(max_heap, (-nums[i], k - 1 + i))
        
        res = []
        time = k - 1
        for i in range(k - 1, len(nums)):
            heapq.heappush(max_heap, (-nums[i], k - 1 + i))
            while max_heap:
                val, expiry_time = max_heap[0]
                if expiry_time < time:
                    heapq.heappop(max_heap)
                else:
                    res.append(-val)
                    break
            time += 1
        return res