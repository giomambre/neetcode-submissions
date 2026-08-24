class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def is_alpha(c):
            c = ord(c)
            if c >= ord("a") and c<=ord("z"):
                return True
            elif c >= ord("A") and c<=ord("Z"):
                return True
            elif c >= ord("0") and c<=ord("9"):
                return True
            return False
        
        L,R = 0 , len(s)-1

        while L <  R:
            
            while not is_alpha(s[L]) and L < R:
                L +=1
            while not is_alpha(s[R]) and L < R:
                R -= 1
            
            if s[L].lower() != s[R].lower():
                return False
            else:
                L+=1
                R-=1
        return True