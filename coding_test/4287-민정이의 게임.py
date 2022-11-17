# -*- coding: utf-8 -*-
import sys


class Maze:
    def __init__(self):
        x, y = map(int, sys.stdin.readline().split())
        self.X = x
        self.Y = y
        self.quotient = 998244353

        self.set_maze()

    def set_maze(self):
        self.Maze = [list(map(int, sys.stdin.readline().split())) for _ in range(self.X)]

    def solution_util(self, x, y):
        if x == self.X - 1 and y == self.Y - 1:
            # print("sucksex")
            return 1
        temp = self.Maze[x][y]
        answer = 0
        # print(x, y)
        self.Maze[x][y] = 10 ** 6

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if x + dx < 0 or y + dy < 0 or x + dx >= self.X or y + dy >= self.Y:
                continue
            if self.Maze[x + dx][y + dy] >= temp:
                continue
            answer += self.solution_util(x + dx, y + dy)

        self.Maze[x][y] = temp
        return answer % self.quotient

    def solution(self):
        # for r in self.Maze:
        #     print(r)
        # return 0
        return (self.solution_util(0, 0))


print(Maze().solution())
