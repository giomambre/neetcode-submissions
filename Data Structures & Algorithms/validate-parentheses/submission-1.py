class Solution:
    def isValid(self, s: str) -> bool:
        
        cls_map = {")" : "(" , "}" : "{", "]" : "["}

        stack = []

        for p in s:
            if p not in cls_map:
                stack.append(p)
            elif len(stack) == 0:
                return False
            else:               
                close = stack.pop()

                if close == cls_map[p]:
                    continue
                else:
                    return False
        
        return len(stack) == 0
