# # method 1 ---> Bruteforce Solution

# class Solution:
#     def is_safe(self, row, col, board, n):
#         d_row = row
#         d_col = col
#         while d_row >= 0 and d_col >= 0:
#             if board[d_row][d_col] == "Q":
#                 return False
#             d_row -= 1
#             d_col -= 1

#         d_row = row
#         d_col = col
#         while d_col >= 0:
#             if board[d_row][d_col] == "Q":
#                 return False
#             d_col -= 1

#         d_row = row
#         d_col = col
#         while d_row < n and d_col >= 0:
#             if board[d_row][d_col] == "Q":
#                 return False
#             d_row += 1
#             d_col -= 1
#         return True

#     def n_queen(self, col, ans, board, n):
#         if col >= n:
#             ans.append(list(board))
#             return

#         for row in range(n):
#             if self.is_safe(row, col, board, n):
#                 board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
#                 self.n_queen(col + 1, ans, board, n)
#                 board[row] = board[row][:col] + "." + board[row][col + 1 :]
#         return ans


# s1 = Solution()
# col = 0
# n = 4
# board = ["." * n for _ in range(n)]
# ans = []
# print(s1.n_queen(col, ans, board, n))


# method 2 ---> Optimal solution
# T.C = O(N!) , S.C = O(N **2)


class Solution:
    def n_queen(self, col, ans, board, leftrow, upper_diagonal, lower_diagonal, n):
        if col == n:
            ans.append(list(board))
            return

        for row in range(n):
            if (
                leftrow[row] == 0
                and upper_diagonal[(n - 1) + (col - row)] == 0
                and lower_diagonal[row + col] == 0
            ):
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                leftrow[row] = 1
                upper_diagonal[(n - 1) + (col - row)] = 1
                lower_diagonal[row + col] = 1
                self.n_queen(
                    col + 1, ans, board, leftrow, upper_diagonal, lower_diagonal, n
                )
                board[row] = board[row][:col] + "." + board[row][col + 1 :]
                leftrow[row] = 0
                upper_diagonal[(n - 1) + (col - row)] = 0
                lower_diagonal[row + col] = 0

    def solveNQueens(self, n):

        board = ["." * n for _ in range(n)]
        leftrow = [0] * n
        upper_diagonal = [0] * (2 * n - 1)
        lower_diagonal = [0] * (2 * n - 1)
        ans = []
        self.n_queen(0, ans, board, leftrow, upper_diagonal, lower_diagonal, n)
        return ans


s1 = Solution()
print(s1.solveNQueens(4))
