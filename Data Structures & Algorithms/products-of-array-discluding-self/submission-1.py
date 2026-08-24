class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1]*n
        suff = [1]*n
        for i in range(len(nums)):
            if i == 0:
                pref[i] = 1
            else :
                pref[i] = pref[i-1] * nums[i-1]

        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suff[i] = 1
            else :
                suff[i] = suff[i+1] * nums[i+1]
        
        res = []


        for i in range(n):
            res.append(pref[i]*suff[i])
        return res

