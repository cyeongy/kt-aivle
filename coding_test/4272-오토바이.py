import sys
from collections import deque


class Maze:
    def __init__(self, n):
        self.N = n
        self.maze = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    def solution(self):
        if self.maze[0][0] == 0:
            return 0

        q = deque([(0, 0)])
        answer = 0
        while q:
            x, y = q.popleft()
            fuel = self.maze[x][y]
            # print(x, y)
            if x == self.N - 1 and y == self.N - 1:
                answer += 1
            if fuel == 0:
                continue
            if x + fuel < self.N:
                q.append((x + fuel, y))
            if y + fuel < self.N:
                q.append((x, y + fuel))

        return answer


n = int(input())
m = Maze(n)
print(m.solution())
