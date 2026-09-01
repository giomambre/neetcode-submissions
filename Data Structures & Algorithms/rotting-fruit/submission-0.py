class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()

        R  = len(grid)
        C  = len(grid[0])   
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        res = 0
        fresh = 0
        def BFS():
            nonlocal res,fresh
            while fresh > 0 and queue:
                res +=1
                for _ in range(len(queue)):

                    r , c = queue.popleft()
                    for dr,dc in neighbors:
                        row , col  = r+dr , c +dc
                        if (row in range(R) 
                        and col in range(C) 
                        and  grid[row][col] == 1
                        ) :
                            grid[row][col] = 2
                            queue.append((row,col))
                            fresh -= 1
                


                       

      
        for r in range(R):
            for c in range(C):

                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh +=1
        BFS()
        return res if fresh == 0 else -1