class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1] * n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                
                # Il valore è la somma di: sopra + sinistra
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # 3. L'angolo in basso a destra contiene la risposta finale
        return dp[m-1][n-1]
        