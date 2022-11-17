import sys
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.Edge = defaultdict(list)

    def addEdge(self, u, v):
        self.Edge[u].append(v)

    def bfs(self):
        dp = [0 for _ in range(self.V + 1)]

        for start in range(1, self.V + 1):
            q = deque(self.Edge[start])
            visited = [False for _ in range(self.V + 1)]
            visited[start] = False
            while q:
                cur = q.popleft()
                visited[cur] = True
                dp[cur] += 1
                for node in self.Edge[cur]:
                    if visited[node]:
                        continue
                    q.append(node)

        return dp

n, m = map(int, sys.stdin.readline().split())
g = Graph(n)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    g.addEdge(u, v)

answer = g.bfs()
value = max(answer)
for i, val in enumerate(answer):
    if val == value:
        print(i, end=' ')