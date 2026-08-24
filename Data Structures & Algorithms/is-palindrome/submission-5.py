class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        

        L , R = 0 , len(s)-1

        while L < R :

            while (not (s[L].isalpha() or s[L].isdigit()) and L < R):
                L+=1
            
            while (not (s[R].isalpha() or s[R].isdigit()) and L < R):
                R-=1
            
            if (s[R].lower() != s[L].lower()):
                return False
            L+=1
            R-=1
        
        return True
