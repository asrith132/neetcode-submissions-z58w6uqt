class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        val_list = self.hashmap[key]
        l = 0
        r = len(val_list) - 1
        ret = ""
        while l <= r:
            mid = (l + r) // 2
            time, res = val_list[mid]
            if timestamp < time:
                r = mid - 1
            elif timestamp > time:
                l = mid + 1
                ret = res
            else:
                return res
        
        return ret
