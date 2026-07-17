class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters = set()
        for word in words:
            for letter in word:
                letters.add(letter)
        
        indegree = {}
        hashmap = {}
        for letter in letters:
            hashmap[letter] = set()
            indegree[letter] = 0

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            length_word1 = len(word1)
            length_word2 = len(word2)
            small_word_length = min(length_word1, length_word2)
            for j in range(0, small_word_length):
                if word1[j] != word2[j]:
                    if word2[j] not in hashmap[word1[j]]:
                        hashmap[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
                elif j == small_word_length - 1:
                    if length_word1 > length_word2:
                        return ""
        queue = deque()
        for letter in letters:
            if indegree[letter] == 0:
                queue.append(letter)

        order = ""
        visited = set()
        while queue:
            letter = queue.popleft()
            order += letter
            for neighbor in hashmap[letter]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        if len(order) != len(letters):
            return ""    
        
        return order

