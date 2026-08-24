class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L , R = 0 , len(nums)-1

        while L <= R:

            middle = ( L + R) // 2

            if nums[middle] == target: 

                return middle
            
            if nums[L] <= nums[middle]:
                # Il target si trova all'interno della metà sinistra ordinata?
                if nums[L] <= target < nums[middle]:
                    R = middle - 1  # Stringiamo a sinistra
                else:
                    L = middle + 1  # Altrimenti andiamo a destra

            # -------------------------------------------------------------
            # CASE 2: La metà DESTRA (da middle a R) è ordinata normalmente
            # -------------------------------------------------------------
            else:
                # Il target si trova all'interno della metà destra ordinata?
                if nums[middle] < target <= nums[R]:
                    L = middle + 1  # Stringiamo a destra
                else:
                    R = middle - 1  # Altrimenti andiamo a sinistra
                    
        return -1