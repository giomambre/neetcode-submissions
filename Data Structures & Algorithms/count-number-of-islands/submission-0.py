class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0

        R = len(grid)
        C = len(grid[0])
        seen = set()

        def dfs(x,y):
            nonlocal res
            if (x,y) in seen or min(x,y) < 0 or x >= R or y >= C or grid[x][y] == "0" :
                return
            seen.add((x,y))
            
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x-1,y)
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs(i,j)
                    res += 1
        
        return res
            