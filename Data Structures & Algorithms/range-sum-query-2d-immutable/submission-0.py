class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R = len(matrix)
        C = len(matrix[0])
        self.M = matrix
        self.pref = [[0] *C for j in range(R)]

        for i in range(R):
            for j in range(C):
                self.pref[i][j] = matrix[i][j]
                if i > 0:
                    self.pref[i][j] += self.pref[i-1][j] 
                if j > 0:
                    self.pref[i][j] += self.pref[i][j-1] 
                if i > 0 and j > 0 :
                    self.pref[i][j] -= self.pref[i-1][j-1]        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        ans = self.pref[row2][col2]
        if row1 > 0:
            ans -= self.pref[row1 - 1][col2]

        if col1 > 0:
            ans -= self.pref[row2][col1 - 1]

        if row1 > 0 and col1 > 0:
            ans += self.pref[row1 - 1][col1 - 1]
        return ans
                


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)