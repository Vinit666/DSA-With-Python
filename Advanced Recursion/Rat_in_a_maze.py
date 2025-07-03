class Solutin:
    def findpath(self, i, j, result, move, maze, n, vis):
        if i == n - 1 and j == n - 1:
            result.append(move)
            return

        # downward
        if i + 1 < n and vis[i + 1][j] == 0 and maze[i + 1][j] == 1:
            vis[i][j] = 1
            self.findpath(i + 1, j, result, move + "D", maze, n, vis)
            vis[i][j] = 0
        # left
        if j - 1 >= 0 and vis[i][j - 1] == 0 and maze[i][j - 1] == 1:
            vis[i][j] = 1
            self.findpath(i, j - 1, result, move + "L", maze, n, vis)
            vis[i][j] = 0

        # right
        if j + 1 < n and vis[i][j + 1] == 0 and maze[i][j + 1] == 1:
            vis[i][j] = 1
            self.findpath(i, j + 1, result, move + "R", maze, n, vis)
            vis[i][j] = 0

        # upward
        if i - 1 >= 0 and vis[i - 1][j] == 0 and maze[i - 1][j] == 1:
            vis[i][j] = 1
            self.findpath(i - 1, j, result, move + "U", maze, n, vis)
            vis[i][j] = 0

    def solve(self):
        maze = [[1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 1, 1, 1]]
        i = 0
        j = 0
        result = []
        move = ""
        n = len(maze)
        vis = [[0] * n for _ in range(n)]
        if maze[i][j] == 1:
            self.findpath(i, j, result, move, maze, n, vis)
        return result
        return vis


s1 = Solutin()
print(s1.solve())
