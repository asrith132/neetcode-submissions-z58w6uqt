class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # (num - 1) * (n + 1) + 1

        hashmap = defaultdict(int)
        max_num = 0
        total_count = len(tasks)
        for i in range(0, len(tasks)):
            hashmap[tasks[i]] += 1
            if hashmap[tasks[i]] > max_num:
                max_num = hashmap[tasks[i]]
        
        max_keys = 0
        for key, val in hashmap.items():
            if val == max_num:
                max_keys += 1

        extra = total_count - (max_keys * max_num)
        downtime = max(0, (n + 1 - max_keys) * (max_num  - 1))
        leftover = max(0, extra - downtime)
        print(extra, downtime)
        return max(len(tasks),(max_num - 1) * (n + 1) + 1 + (max_keys - 1) + leftover)

        # A B * * A B * *
        
        
