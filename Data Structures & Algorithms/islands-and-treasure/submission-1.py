class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        candidates = [(0,1),(0,-1),(1,0),(-1,0)]

        R = len(grid)
        C = len(grid[0])
        queue = deque((i,j) for i in range(R) for j in range(C) if grid[i][j] == 0)
        cur_dist = 0
        while queue:

            cur_dist +=1
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in candidates:

                    if min(r+dr,c+dc) < 0 or r+dr >= R or c+dc >= C or grid[r+dr][c+dc] ==-1:
                        continue

                    if grid[r+dr][c+dc] > cur_dist:
                        grid[r+dr][c+dc] = cur_dist
                        queue.append((r+dr,c+dc))
            



            

        