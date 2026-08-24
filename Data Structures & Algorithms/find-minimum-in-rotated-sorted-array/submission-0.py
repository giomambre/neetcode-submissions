class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L , R  = 0 , len(nums)-1

        while L < R:

            middle = (L + R) // 2

            if nums[middle] >= nums[R]:
                L = middle  + 1
            else:
                R = middle  
        
        return nums[R]