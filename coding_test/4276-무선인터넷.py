import sys
from collections import deque


class Graph:
    def __init__(self):
        self.X = int(sys.stdin.readline())
        self.maze = [list(map(int,sys.stdin.readline().split())) for _ in range(self.X)]
        self.router = []
        self.house = []
        for x, line in enumerate(self.maze):
            for y, val in enumerate(line):
                if val == 2:
                    self.router.append((x, y))
                elif val == 1:
                    self.house.append((x, y))

    def bfs(self):

        pass

    def solution(self):
        answer = 10e8
        for x, y in self.router:
            val = 0
            for dx, dy in self.house:
                val += abs(x-dx) + abs(y-dy)
            answer = min(answer, val)
        return answer


g = Graph()
print(g.solution() if g.solution() != 10 ** 9 else -1)
