class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        neigh = [(1,0), (-1,0), (0,1), (0,-1)]
        used = set()

        def dfs(r, c):
            # Fuori dalla griglia = un lato del perimetro
            if r < 0 or c < 0 or r >= R or c >= C:
                return 1

            # Acqua = un lato del perimetro
            if grid[r][c] == 0:
                return 1

            # Terra già visitata = nessun nuovo perimetro
            if (r, c) in used:
                return 0

            used.add((r, c))

            perimeter = 0

            for dr, dc in neigh:
                perimeter += dfs(r + dr, c + dc)

            return perimeter

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return dfs(r, c)

        return 0