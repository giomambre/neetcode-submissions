class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        pt1 = 0
        pt2 = 0
        res = ""
        while pt1 < len(word1) and pt2 < len(word2):
            
            res+=word1[pt1]
            res+=word2[pt2]

            pt1 +=1
            pt2 +=1 
        
        if pt1 < len(word1):
            return res + word1[pt1:]
        if pt2 < len(word2):
            return res + word2[pt2:]
        
        return res