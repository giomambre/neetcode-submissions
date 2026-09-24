class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mask_s = [0]*26
        mask_t = [0]*26

        for i in s:
            mask_s[ord(i)- ord("a")] +=1
        
        for i in t:
            mask_t[ord(i)- ord("a")] +=1

        
        return mask_s == mask_t