class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for n in nums:
            if (n-1) not in numset:
                j = 1
                while n+j in numset:
                    j+=1
                res = max(res,j)
                 
        return res