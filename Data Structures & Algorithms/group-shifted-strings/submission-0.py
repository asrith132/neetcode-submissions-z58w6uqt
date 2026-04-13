class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strings:
            key = [0] * 26
            first_letter = word[0]
            for letter in word:
                key[ord(letter) - ord(first_letter)] += 1
            hashmap[tuple(key)].append(word)
        return list(hashmap.values())
        