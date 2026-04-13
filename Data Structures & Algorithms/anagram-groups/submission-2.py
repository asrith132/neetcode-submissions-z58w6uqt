from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for letters in word:
                freq[ord(letters) - ord('a')] += 1
            hashmap[tuple(freq)].append(word)
        
        return list(hashmap.values())
        
