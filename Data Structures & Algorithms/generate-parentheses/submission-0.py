class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = ""

        def backT(O, C):
            nonlocal curr

            if O == C == n:
                res.append(curr)
                return

            if O < n:
                curr += "("
                backT(O + 1, C)
                curr = curr[:-1]

            if C < O:
                curr += ")"
                backT(O, C + 1)
                curr = curr[:-1]

        backT(0, 0)
        return res