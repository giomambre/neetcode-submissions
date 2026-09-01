class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        L , R = 0 , len(nums)-1
        while L < R:
            mid = nums[L] + nums[R]
            if mid == target:
                return [L+1,R+1]
            if mid > target:
                R -=1
            else:
                L+=1
