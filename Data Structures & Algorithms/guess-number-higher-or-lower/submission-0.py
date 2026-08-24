# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        L = 0
        R = n

        while  L <= R:
            M = (L + R) //2

            res = guess(M)

            if res == 0:
                return M
            
            if res == 1:

                L = M +1
            else:
                R = M - 1
        
        return 0