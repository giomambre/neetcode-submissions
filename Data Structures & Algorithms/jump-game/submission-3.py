class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1,2,0,1,0]

        max_reach = 0
        target = len(nums)-1
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= target:
                return True
       