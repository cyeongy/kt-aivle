import sys
from collections import deque
from copy import deepcopy


class Maze:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.maze = []

    def add_maze(self, x):
        self.maze.append(x)

    def solution(self):
        q = deque()
        cat = (0, 0)
        paints = []
        for x, line in enumerate(self.maze):
            for y, val in enumerate(line):

                if val == 2:
                    paints.append((x, y))
                if val == 1:
                    cat = (x, y)
        q.append((cat, paints, self.maze, 1))

        while q:
            cat, paints, maze, cost = q.popleft()
            new_paints = []
            # 색칠하기
            for x, y in paints:
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if x+dx < 0 or y+dy < 0 or x+dx >= self.X or y+dy >= self.Y:
                        continue
                    if maze[x+dx][y+dy] < 2:
                        maze[x+dx][y+dy] = 2
                        new_paints.append((x+dx, y+dy))

            x, y = cat

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if x + dx < 0 or y + dy < 0 or x + dx >= self.X or y + dy >= self.Y:
                    return cost
                if maze[x + dx][y + dy] == 0:
                    maze[x+dx][y+dy] = 1
                    q.append(((x+dx, y+dy), new_paints, deepcopy(maze), cost+1))
                    # for i in maze:
                    #     print(i)
                    # print("--" * 10)

        return "IMPOSSIBLE"


n, m = map(int, sys.stdin.readline().split())

maze = Maze(n, m)
for _ in range(n):
    maze.add_maze(list(map(int, sys.stdin.readline().split())))

print(maze.solution())
