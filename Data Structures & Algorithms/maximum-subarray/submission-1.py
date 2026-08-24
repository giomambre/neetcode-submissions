class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = nums[0]
        res = nums[0]

        for n in nums[1:]:
            curr = max(curr + n , n)
            
            res = max(res,curr)
        return res