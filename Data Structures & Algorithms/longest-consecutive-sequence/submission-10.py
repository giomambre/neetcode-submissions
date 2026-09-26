class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        res = 0

        for n in nums:
            if n-1 in seen:
                continue
            i = 1

            while n + i in seen:
                i+=1
            
            res = max(res, i )
        
        return res
            