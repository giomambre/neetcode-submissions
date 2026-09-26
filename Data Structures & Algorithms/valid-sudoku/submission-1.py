class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[j] 
                or board[i][j] in cols[i]
                or board[i][j] in squares[(i//3,j//3)]):
                    return False
                
                el = board[i][j]
                rows[j].add(el)
                cols[i].add(el)
                squares[(i//3,j//3)].add(el)

        return True

            