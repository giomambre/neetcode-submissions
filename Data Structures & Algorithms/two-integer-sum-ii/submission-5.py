class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers)-1

        while L < R:
            cur_sum = numbers[L] + numbers[R]

            if cur_sum == target:
                return [L+1,R+1]
            elif cur_sum < target:
                L +=1
            else:
                R -= 1
        