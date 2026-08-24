from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n):
            pivot = nums[i]
            
            
            if pivot > 0:
                break
                
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            L = i + 1
            R = n - 1
            
            while L < R:
                curr = pivot + nums[L] + nums[R]
                
                if curr == 0:
                    res.append([pivot, nums[L], nums[R]])
                    
                    L += 1
                    R -= 1
                    
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                        
                elif curr > 0:
                    R -= 1
                else:
                    L += 1
        
        return res