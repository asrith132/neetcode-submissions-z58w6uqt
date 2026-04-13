class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        max_freq = max(freq)
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        res = ""
        while len(res) < len(s):
            maxIdx = freq.index(max(freq))
            char = chr(maxIdx + ord('a'))
            res += char
            freq[maxIdx] -= 1
            if freq[maxIdx] == 0:
                continue

            temp = freq[maxIdx]
            freq[maxIdx] = -1
            nextMaxIdx = freq.index(max(freq))
            nextChar = chr(nextMaxIdx + ord('a'))
            res += nextChar
            freq[maxIdx] = temp
            freq[nextMaxIdx] -= 1

        return res
        