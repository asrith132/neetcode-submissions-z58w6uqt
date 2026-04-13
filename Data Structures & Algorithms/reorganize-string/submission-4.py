import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_val = list(counter.values())[0]
        if max_val >= len(s) / 2 + 1:
            return ""
        
        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, (-1 * v, k))

        res = ""
        while heap:
            v, k = heapq.heappop(heap)
            new_v = v + 1
            res += k
            if new_v == 0:
                continue
            
            next_v, next_k = heapq.heappop(heap)
            next_new_v = next_v + 1
            res += next_k
            heapq.heappush(heap, (new_v, k))
            if next_new_v == 0:
                continue
            heapq.heappush(heap, (next_new_v, next_k))

        return res

        