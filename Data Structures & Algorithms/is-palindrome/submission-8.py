class Solution:
    def isPalindrome(self, s: str) -> bool:
        #check first character and last character
        #left and right pointers until the two indices are the same or pass each other, then stop

        left = 0
        right = len(s)-1

        while(left < right):
            while(not s[left].isalnum() and not len(s) == (left+1)):
                left+=1 #1
            while(not s[right].isalnum() and not -1 == (right-1)):
                right-=1 #0
            if(s[left].lower() != s[right].lower() and left < right):
                return False
            left+=1
            right-=1
    

        return True