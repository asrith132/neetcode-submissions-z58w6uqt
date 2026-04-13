class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)

        prev_time = None
        res = []
        for index, interval in enumerate(intervals):
            start, end = interval
            if prev_time:
                if start <= prev_time:
                    prev_start, prev_end = res[-1]
                    res[-1][0] = min(prev_start, start)
                    res[-1][1] = max(prev_end, end) 
                    prev_time = res[-1][1]
                else:
                    res.append(interval)
                    prev_time = end
            else:
                prev_time = end
                res.append(interval)
        return res