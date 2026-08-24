from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        if len(word) > R * C:
            return False

        board_count = Counter(
            board[r][c]
            for r in range(R)
            for c in range(C)
        )

        word_count = Counter(word)

        for ch, cnt in word_count.items():
            if board_count[ch] < cnt:
                return False

        # Inizia dal carattere più raro
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        N = len(word)

        def dfs(r, c, k):
            if board[r][c] != word[k]:
                return False

            if k == N - 1:
                return True

            ch = board[r][c]
            board[r][c] = "#"

            nk = k + 1

            if r > 0 and board[r - 1][c] == word[nk]:
                if dfs(r - 1, c, nk):
                    board[r][c] = ch
                    return True

            if r + 1 < R and board[r + 1][c] == word[nk]:
                if dfs(r + 1, c, nk):
                    board[r][c] = ch
                    return True

            if c > 0 and board[r][c - 1] == word[nk]:
                if dfs(r, c - 1, nk):
                    board[r][c] = ch
                    return True

            if c + 1 < C and board[r][c + 1] == word[nk]:
                if dfs(r, c + 1, nk):
                    board[r][c] = ch
                    return True

            board[r][c] = ch
            return False

        first = word[0]

        for r in range(R):
            for c in range(C):
                if board[r][c] == first and dfs(r, c, 0):
                    return True

        return False