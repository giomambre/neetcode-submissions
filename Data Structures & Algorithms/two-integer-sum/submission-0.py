class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Avoid using 'map' as a variable name since it's a built-in Python function

        for i, n in enumerate(nums):  # Using enumerate is cleaner and more Pythonic
            complement = target - n
            
            if complement in seen:
                return [seen[complement], i]
            
            # Store the CURRENT number and its index
            seen[n] = i