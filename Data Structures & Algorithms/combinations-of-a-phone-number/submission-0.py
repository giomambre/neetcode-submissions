class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        curr = ""
        N = len(digits)
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backT(i):
            nonlocal curr
            if i >= N:
                res.append(curr)
                return
            for c in digitToChar[digits[i]]:
                curr += c
                backT(i+1)
                curr = curr[:-1]
                
        
        if digits:
            backT(0)
        return res


            



