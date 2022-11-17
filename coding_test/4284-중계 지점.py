# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict


class Graph:
    def __init__(self, vertices):
        # V : 노드 개수
        self.V = vertices
        self.graph = defaultdict(list)

    # 간선 추가
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def Dijkstra(self, start):
        q = deque([start])
        distance = [1e9] * (self.V + 1)
        distance[0] = distance[start] = 0

        while q:
            src = q.popleft()
            for dst in self.graph[src]:
                if distance[src] + 1 < distance[dst]:
                    distance[dst] = distance[src] + 1

                    for _next in self.graph[dst]:
                        if distance[dst] + 1 < distance[_next]:
                            q.append(dst)

        return max(distance)

    def solution(self):
        answer = (10e9, 0)
        for i in range(1, self.V + 1):
            answer = min((self.Dijkstra(i), i), answer)
        return answer


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = Graph(n)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph.addEdge(u, v)

print(graph.solution()[1])
