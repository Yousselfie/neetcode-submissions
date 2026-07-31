class Solution:
    def isValid(self, s: str) -> bool:
        legend = {")":"(", "}":"{", "]":"["}
        stack = []
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
                return False
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            if char == ")" or char == "]" or char == "}":
                if len(stack) == 0 or not stack.pop() == legend[char]: return False
            

        return len(stack)==0
            
            