# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.


from itertools import product


class Solution(object):
    def solve(self, board):
        if not board: return 0

        self.board, self.width, self.height = board, len(board), len(board[0])
        self.x_mark, self.o_mark, self.t_mark = 'X', 'O', 'TEMP'

        for i in range(0, self.width):
            self.dfs(i, 0)
            self.dfs(i, self.height - 1)

        for j in range(0, self.height):
            self.dfs(0, j)
            self.dfs(self.width - 1, j)

        for i, j in product(range(self.width), range(self.height)):
            board[i][j] = self.x_mark if board[i][j] != self.t_mark else self.o_mark

    def dfs(self, i, j):
        if (
            i < 0
            or j < 0
            or i >= self.width
            or j >= self.height
            or self.board[i][j] != self.o_mark
        ):
            return

        self.board[i][j] = self.t_mark
        neib_list = [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]

        for x, y in neib_list:
            self.dfs(x, y)
