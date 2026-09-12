class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(0, len(s)):
            hashmap[s[i]] = i

        res = []
        l = 0
        i = 0
        r = hashmap[s[i]]
        total = 0
        while i < len(s):
            r = max(hashmap[s[i]], r)
            if r == i:
                res.append(r - l + 1)
                total += r - l + 1
                i += 1
                l = i
                r = 0
            else:
                i += 1

        if len(s) - total > 0:
            res.append(len(s) - total)
        return res


