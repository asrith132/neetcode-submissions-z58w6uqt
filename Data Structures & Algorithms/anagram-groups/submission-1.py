class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for i in strs:
            sorted_i = sorted(i)
            anagram[tuple(sorted_i)].append(i)
        return list(anagram.values())