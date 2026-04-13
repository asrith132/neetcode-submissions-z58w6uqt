class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            final += str(len(s)) + "#" + s
        final += "-1#"
        print(final)
        return final

    def decode(self, s: str) -> List[str]:
        if (s == "0#0"):
            return [""]
        final = []
        index = 0
        count = 0
        strC = ""
        for char in s:
            if (char == "#"):
                break
            else:
                strC += char
        count = int(strC)
        while (count != -1):
            buff = len(str(count))
            val = s[index+1 + buff:count+1 + buff]
            s = s[count + 1 + buff: len(s)]
            final.append(val)
            strC = ""
            for char in s:
                if (char == "#"):
                    break
                else:
                    strC += char
            count = int(strC)
        print(final)
        return final

