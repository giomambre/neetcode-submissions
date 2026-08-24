class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Se il numero corrente è > 0, non possono esserci triplette (array ordinato)
            if nums[i] > 0:
                break
            
            # Salta i duplicati per il primo elemento
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L, R = i + 1, len(nums) - 1

            while L < R:
                current_sum = nums[i] + nums[L] + nums[R]

                if current_sum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    
                    # Sposta i puntatori e salta i duplicati
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    
                    L += 1
                    R -= 1
                elif current_sum < 0:
                    L += 1
                else:
                    R -= 1

        return res