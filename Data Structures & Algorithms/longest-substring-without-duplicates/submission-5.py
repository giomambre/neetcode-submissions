class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        window = set()
        L , R = 0 , 0
        res = 0
        for i in range(len(s)):

            if s[R] not in window:
                window.add(s[R])
                res = max(res,len(window))
                R+=1
                
            else:
                while s[R] in window:
                    window.remove(s[L])
                    L+=1
                window.add(s[R])
                res = max(res,len(window))
                R+=1
            
        return res

