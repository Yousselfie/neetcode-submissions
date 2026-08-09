class Solution:

    def encode(self, strs: List[str]) -> str:
        #delimiter before each word will be n (the len of the string) + '#'
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            if s[i] == '#' and s[0:i].isnumeric():
                length = int(s[0:i])
                word = s[i+1:i+1+length]
                res.append(word)
                s = s[i+1+length:]
                i=0
            else:
                i+=1
        return res
        