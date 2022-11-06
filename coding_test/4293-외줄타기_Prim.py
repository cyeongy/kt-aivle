import sys
from collections import defaultdict
from heapq import heappush, heappop


class Prim:
    def __init__(self, v):
        self.vertices = v
        self.edges = defaultdict(list)

    def addEdge(self, a, b, c):
        self.edges[a].append((b, c))
        self.edges[b].append((a, c))

    def find(self):
        answer = 0
        q = []
        visited = [0] * (self.vertices + 1)

        visited[1] = 1
        for b, c in self.edges[1]:
            heappush(q, (c, 1, b))

        while sum(visited) != self.vertices:
            _c, _a, _b = heappop(q)
            if visited[_a] == 1 and visited[_b] == 1:
                continue

            if visited[_a] != 1:
                for __b, __c in self.edges[_a]:
                    heappush(q, (__c, _a, __b))

            if visited[_b] != 1:
                for __a, __c in self.edges[_b]:
                    heappush(q, (__c, _b, __a))

            visited[_a] = 1
            visited[_b] = 1
            answer += _c

        return answer


v, e = map(int, sys.stdin.readline().split())
solution = Prim(v)
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    solution.addEdge(a, b, c)

print(solution.find())
