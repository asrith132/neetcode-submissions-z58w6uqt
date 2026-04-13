class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        ret = []
        for n in nums:
            hashMap[n] = hashMap[n] + 1
        
        for i in range(k):
            maximum = -1;
            store = -1;
            for key in hashMap:
                if (hashMap[key] > maximum):
                    store = key;
                    maximum = hashMap[key]
            ret.append(store)
            hashMap[store] = -1
        
        return ret
        