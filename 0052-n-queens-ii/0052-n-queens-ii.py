class Solution:
    def totalNQueens(self, n: int) -> int:
        columns = set()
        diagonal_p = set()
        diagonal_n = set()

        soln = 0
        board = [["."] * n for _ in range(n)]
        def backtrack(row):
            nonlocal soln
            if row == n:
                soln += 1
                return
            for col in range(n):
                dp = row + col
                dn = row - col
                if col in columns or dp in diagonal_p or dn in diagonal_n:
                   continue
                columns.add(col)
                diagonal_p.add(dp)
                diagonal_n.add(dn)
                board[row][col] = "Q"

                backtrack(row + 1)

                columns.remove(col)
                diagonal_p.remove(dp)
                diagonal_n.remove(dn)
                board[row][col] = "."
        backtrack(0)
        return soln

