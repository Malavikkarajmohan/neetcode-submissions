class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in range(len(strs)):
            encoded_str += str(len(strs[i])) + "#" + strs[i]
        return encoded_str

    def decode(self, s: str) -> List[str]:
        print(s)
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
                print(s[i:j])
                length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

        


