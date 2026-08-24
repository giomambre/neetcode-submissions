class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # tempo = dist / vel
        # dist = target - pos

        # 
        
        cars = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        
        cars.sort(key = lambda x:x[0] , reverse = True)
        
        stack = []

        for pos , v in cars:

            t = (target - pos) / v

            stack.append(t)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        print(stack)
        return len(stack)

