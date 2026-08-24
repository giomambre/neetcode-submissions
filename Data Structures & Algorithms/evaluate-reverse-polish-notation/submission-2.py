class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+", "-", "*", "/"}

        for tk in tokens:

            if tk in "/+-*":
                a = stack.pop()
                b = stack.pop()

                if tk == "+":
                    stack.append(b + a)
                elif tk == "-":
                    stack.append(b - a)
                elif tk == "*":
                    stack.append(b * a)
                elif tk == "/":
                    stack.append(int(b / a))

            else:
                stack.append(int(tk))

        return stack[0]