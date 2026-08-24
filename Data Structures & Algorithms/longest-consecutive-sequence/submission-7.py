class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setOcc = set(nums)
        res = 0
        for n in setOcc:
            if n-1 not in setOcc:
                cur = n+1
                tmp = 1
                while cur in setOcc:
                    cur+=1
                    tmp+=1
                
                res = max(res,tmp)
        return res
                    
