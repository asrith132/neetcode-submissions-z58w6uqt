class Solution:
    import math

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = min_answer = max(piles)

        while low <= high:
            mid = (low + high) // 2
            
            hours_needed = 0
            for i in piles:
                hours_needed += math.ceil(i/mid)

            if hours_needed <= h:
                min_answer = min(min_answer, int(mid))
                high = mid - 1
            else:
                low = mid + 1
        
        return min_answer

        