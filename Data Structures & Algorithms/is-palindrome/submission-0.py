class Solution:
    def isPalindrome(self, s: str) -> bool:
        #split the string
        #join the string
        #check if reverse == string
        ls = list(s)
        joined = "".join(char.lower() for char in ls if char.isalnum())
        return joined == joined[::-1]