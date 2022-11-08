# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
from heapq import heappush, heappop


class Graph:
    def __init__(self, vertices):
        # V : 노드 개수
        self.V = vertices
        self.graph = defaultdict(list)

    # 간선 추가
    def addEdge(self, v, w, c):
        self.graph[v].append((w, c))

    def Dijkstra(self, start, end):
        q = []
        distance = [1e9] * (self.V + 1)
        distance[start] = 0
        for _next, _cost in self.graph[start]:
            heappush(q, (_cost, start, _next))

        while q:
            cost, src, dst = heappop(q)
            if distance[src] + cost < distance[dst]:
                distance[dst] = distance[src] + cost

                for _next, _cost in self.graph[dst]:
                    if distance[dst] + _cost < distance[_next]:
                        heappush(q, (_cost, dst, _next))
            pass
        return distance[end]


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = Graph(n)

for _ in range(m):
    v, w, c = map(int, sys.stdin.readline().split())
    graph.addEdge(v, w, c)

s, e = map(int, sys.stdin.readline().split())
print(graph.Dijkstra(s, e))
