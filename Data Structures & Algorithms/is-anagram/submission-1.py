class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:
            if s.count(c)!=t.count(c):
                return False
        return len(s) == len(t)
        