class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        ans = ""

        n = len(strs)
        if n == 0 :
            return ans 

        for i in range(len(strs[0])):

        
            
            ans += strs[0][i]
            
            for j in range(n):
                if i >= len(strs[j]) or strs[j][i] != ans[-1]:
                    return ans[:-1]

            


        return ans 
