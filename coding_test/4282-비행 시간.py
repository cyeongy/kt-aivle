# -*- coding: utf-8 -*-
import sys
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        # V : 노드 개수
        self.V = vertices
        self.graph = [[0 for _ in range(self.V)] for _ in range(self.V)]

    # 간선 추가
    def addEdge(self, v, w, c):
        self.graph[v - 1][w - 1] = c

    def floyd_warshall(self):
        dp = [[0 for _ in range(self.V)] for _ in range(self.V)]

        for _ in range(2):
            for mid in range(self.V):
                for src in range(self.V):
                    for dst in range(self.V):
                        if self.graph[src][mid] == 0 or self.graph[mid][dst] == 0:
                            continue

                        if self.graph[src][dst] == 0:
                            self.graph[src][dst] = self.graph[src][mid] + self.graph[mid][dst]
                        elif self.graph[src][dst] > self.graph[src][mid] + self.graph[mid][dst]:
                            self.graph[src][dst] = self.graph[src][mid] + self.graph[mid][dst]

        return self.graph


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = Graph(n)

for _ in range(m):
    v, w, c = map(int, sys.stdin.readline().split())
    graph.addEdge(v, w, c)

for x in graph.floyd_warshall():
    print(' '.join(map(str, x)))
