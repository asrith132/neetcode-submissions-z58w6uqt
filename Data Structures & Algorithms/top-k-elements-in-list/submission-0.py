from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        results = []
        for i, n in enumerate(nums):
            hashMap[n] += 1
        
        i = 0
        while (i < k):
            j = len(hashMap)
            current_max = 0
            current_index = 0
            for key in hashMap:
                if (hashMap[key] > current_max):
                    current_max = hashMap[key];
                    current_index = key;
            results.append(current_index)
            hashMap[current_index] = -1
            i = i + 1
        
        return results

    
