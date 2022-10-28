import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
import copy
from collections import deque, defaultdict, Counter
from fractions import Fraction
import time
from heapq import heappush as push, heappop as pop


class Graph:
    def __init__(self, vertices):
        # V : 노드 개수
        self.V = vertices
        self.graph = defaultdict(list)

    # 간선 추가
    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent):

        # 방문 기록 남기기
        visited[v] = True
        print(v+1)
        for i in self.graph[v]:
            # 방문하지 않은 노드 확인
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, v)):
                    return True
            # 부모 제외하고 재방문가능하면 무한루프 가능함
            elif parent != i:
                if v == 1:
                    continue
                return True

        return False

    def isCyclic(self):

        visited = [False] * (self.V)

        # 방문하지 않은 노드 확인 1번부터 시작
        for i in range(1):
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, -1)):
                    return True

        return False


N, M = map(int, sys.stdin.readline().split())
g = Graph(N)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    g.addEdge(u - 1, v - 1)

if g.isCyclic():
    print("YES")
else:
    print("NO")
