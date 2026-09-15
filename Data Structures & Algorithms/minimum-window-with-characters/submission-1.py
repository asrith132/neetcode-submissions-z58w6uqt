class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #store the letters of t in a hashmap storing the letter of t and how many instances you r looking for
        #travese the string from left to right once you hit a letter keep the left point at that spot and increment the right pointer until you find everything you are looking for
        #keep a counter seeing how many letters u r still looking for
        #if the counter hits zero store that string in result
        #after that you can increment the left pointer and add back that instance in the hashmap then you can look for the next instance of the right pointer

        hashmap = defaultdict(int)
        counter = len(t)
        for letter in t:
            hashmap[letter] += 1

        length = len(s)
        l = 0
        r = 0
        rl = float('inf')
        resl = l
        resr = r
        while l < length and (r < length or counter == 0):
            if counter == 0:
                if rl > (r - l + 1):
                        rl = r - l + 1
                        resl = l
                        resr = r
                if s[l] in hashmap.keys():
                    hashmap[s[l]] += 1
                    if hashmap[s[l]] > 0:
                        counter += 1                
                l += 1
            else:
                if s[r] in hashmap.keys():
                    if hashmap[s[r]] > 0:
                        counter -= 1
                    hashmap[s[r]] -= 1
                r += 1
        
        return s[resl:resr]

        
