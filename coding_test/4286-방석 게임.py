import sys
from itertools import permutations
from collections import defaultdict, deque
from copy import deepcopy


class Maze:
    def __init__(self, x: int, y: int) -> None:
        self.distance = defaultdict(lambda: defaultdict(lambda: 10**9))
        self.X = x
        self.Y = y
        self.students = []
        self.places = []

        self.set_maze()

    def set_maze(self) -> None:
        self.maze = [list(sys.stdin.readline()) for _ in range(self.X)]

        for row, x in enumerate(self.maze):
            for col, y in enumerate(x):
                if y == 'P':
                    self.places.append((row, col))
                elif y == 'C':
                    self.students.append((row, col))

    def solution_util(self):
        answer = 0

        for src, (x, y) in enumerate(self.students):
            q = deque([(x, y)])
            count = 0
            maze = deepcopy(self.maze)
            while count < len(self.places) and q:
                maze[x][y] = 'X'
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if x + dx < 0 or y + dy < 0 or x + dx >= self.X or y + dy >= self.Y:
                        continue
                    if maze[x + dx][y + dy] == 'X':
                        continue

        return answer

    def solution(self) -> int:
        return 0


x, y = map(int, sys.stdin.readline().split())
m = Maze(x, y)

print(m.solution())

print(list(permutations([(0, 0), (1, 1,), (2, 2), (3, 3)])))