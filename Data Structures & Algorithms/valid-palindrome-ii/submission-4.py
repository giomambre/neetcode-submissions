class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def checkPath(s):

            L = 0
            R = len(s)-1

            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            
            return True

        
        L = 0
        R = len(s)-1
        while L < R:
            if s[L] != s[R]:

                return checkPath(s[L+1:R+1]) or checkPath(s[L:R]) 
            L +=1
            R -= 1
        return True