import sys


class Graph:
    def __init__(self):
        self.X, self.Y = map(int, sys.stdin.readline().split())

        self.maze = [list(sys.stdin.readline().strip()) for _ in range(self.X)]

    def solution_util(self, x, y, cost, count):
        if x == self.X - 1 and y == self.Y - 1:
            return cost
        # print(self.maze)
        old_value = self.maze[x][y]
        self.maze[x][y] = 'x'
        answer = 10 ** 9
        for dx, dy in  [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if x + dx < 0 or y + dy < 0 or x + dx >= self.X or y + dy >= self.Y:
                continue
            if self.maze[x+dx][y+dy] == 'x':
                continue
            if self.maze[x+dx][y+dy] == '0':
                answer = min(self.solution_util(x+dx, y+dy, cost+1, count), answer)
            elif count > 0:
                answer = min(self.solution_util(x+dx, y+dy, cost+1, 0), answer)
        self.maze[x][y] = old_value
        return answer

        pass

    def solution(self):
        return self.solution_util(0, 0, 1, 1)

g = Graph()
print(g.solution() if g.solution() != 10**9 else -1)