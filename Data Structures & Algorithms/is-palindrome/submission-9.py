class Solution:

    def isAlphanumeric(self, n: str) -> bool:
        ascii_n = ord(n)
        return (ascii_n >= 48 and ascii_n<=57) or (ascii_n>=65 and ascii_n<=90) or (ascii_n>=97 and ascii_n<=122)

    def isPalindrome(self, s: str) -> bool:
        #check first character and last character
        #left and right pointers until the two indices are the same or pass each other, then stop
        #check ascii values of chars to keep only alpha num

        left = 0
        right = len(s)-1

        while(left < right):
            while(not self.isAlphanumeric(s[left]) and not len(s) == (left+1)):
                left+=1 #1
            while(not self.isAlphanumeric(s[right]) and not -1 == (right-1)):
                right-=1 #0
            if(s[left].lower() != s[right].lower() and left < right):
                return False
            left+=1
            right-=1
    

        return True