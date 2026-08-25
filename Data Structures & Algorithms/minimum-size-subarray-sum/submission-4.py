class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        res = float("+inf")

        L, R = 0, 0
        
        # R deve poter arrivare fino a len(nums)
        while R < len(nums) or curr_sum >= target:
            
            if curr_sum < target:
                curr_sum += nums[R]
                R += 1
            else:
                res = min(res, R - L)
                curr_sum -= nums[L]
                L += 1

        return res if res != float("+inf") else 0