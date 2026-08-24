class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i in range(len(nums)):

            tmp = target - nums[i]

            if tmp not in map:
                map[nums[i]] = i
            else:
                return [map[tmp],i]
        
        return []
        


            
