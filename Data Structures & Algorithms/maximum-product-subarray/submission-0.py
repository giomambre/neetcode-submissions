class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        result = nums[0]

        for num in nums[1:]:
            previous_max = cur_max

            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * previous_max, num * cur_min)

            result = max(result, cur_max)

        return result