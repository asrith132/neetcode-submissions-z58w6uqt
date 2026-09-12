class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = newInterval[0]
        r = newInterval[1]
        res = []
        prev = float('-inf')
        i = 0
        l_found = False
        r_found = False
        while i < len(intervals):
            if not l_found:
                if prev < l and l < intervals[i][0]:
                    newInterval[0] = l
                    l_found = True
                elif intervals[i][0] <= l and l <= intervals[i][1]:
                    newInterval[0] = min(intervals[i][0], l)
                    l_found = True
                else:
                    res.append(intervals[i])
                    i += 1
            elif not r_found:
                if r < intervals[i][0]:
                    res.append(newInterval)
                    r_found = True
                elif r <= intervals[i][1]:
                    newInterval[1] = max(r, intervals[i][1])
                    res.append(newInterval)
                    i += 1
                    r_found = True
                else:
                    i += 1
            else:
                res.append(intervals[i])
                i += 1
        if not r_found:
            res.append(newInterval)
        return res
            

