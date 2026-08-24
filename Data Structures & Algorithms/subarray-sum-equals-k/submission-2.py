from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefToCount = defaultdict(int)

        prefToCount[0] = 1
        curSum = 0
        res = 0

        for n in nums:
            curSum += n

            res += prefToCount[curSum - k]
            
            prefToCount[curSum] += 1
        
        return res