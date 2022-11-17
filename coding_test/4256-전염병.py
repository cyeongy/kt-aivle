import sys
from collections import deque
from functools import reduce


class Graph:
    def __init__(self, x, y):
        self.maze = None
        self.X = x
        self.Y = y

        self.set_maze()

    def set_maze(self):
        self.maze = [list(map(int, sys.stdin.readline().split())) for _ in range(self.X)]

    def solution(self):
        q = deque()
        dp = [[0 for _ in range(self.Y)] for _ in range(self.X)]
        for x, line in enumerate(self.maze):
            for y, val in enumerate(line):
                if val == 1:
                    q.append((x, y, 0))
                    dp[x][y] = 1
                if val == 2 or val == -1:
                    dp[x][y] = 1
        if reduce(lambda a, b: a + sum(b), dp, 0) == self.X * self.Y:
            return 0
        while q:
            x, y, cost = q.popleft()
            if reduce(lambda a, b: a + sum(b), dp, 0) == self.X * self.Y:
                return cost
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if x + dx < 0 or y + dy < 0 or x + dx >= self.X or y + dy >= self.Y:
                    continue
                if dp[x + dx][y + dy] <= 0:
                    dp[x + dx][y + dy] = 1
                    q.append((x + dx, y + dy, cost + 1))

        return -1


n, m = map(int, sys.stdin.readline().split())
g = Graph(n, m)
print(g.solution())
