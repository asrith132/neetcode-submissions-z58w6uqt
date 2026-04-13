class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = {}
        for letter in s:
            hashmap[letter] = hashmap.get(letter, 0) + 1
        arr = [0] * 26

        for k, v in hashmap.items():
            if v > math.ceil(len(s) / 2):
                return ""
            arr[ord(k) - ord('a')] = v
            
        res = ""
        for i in range(0, len(s)//2):

            max_idx = 0
            max_occurence = -1
            for i, v in enumerate(arr):
                if max_occurence < v:
                    max_occurence = v
                    max_idx = i
                    
            char = chr(ord('a') + max_idx)
            temp_val = arr[max_idx] - 1
            arr[max_idx] = -1
            res += char

            s_max_idx = 0
            max_occurence = -1
            for i, v in enumerate(arr):
                if max_occurence < v:
                    max_occurence = v
                    s_max_idx = i
            s_char = chr(ord('a') + s_max_idx)
            
            arr[s_max_idx] -= 1
        
            arr[max_idx] = temp_val
            res += s_char
        
        if len(s) % 2 == 1:
            max_idx = 0
            max_occurence = -1
            for i, v in enumerate(arr):
                if max_occurence < v:
                    max_occurence = v
                    max_idx = i
                    
            char = chr(ord('a') + max_idx)
            arr[max_idx] -= 1
            res += char
        return res

