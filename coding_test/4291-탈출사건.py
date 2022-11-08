# -*- coding: utf-8 -*-
import sys
from collections import deque
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

empties = []
jags = []

answer = 0


def bfs():
    _map = deepcopy(arr)
    q = deque(jags)

    while q:
        x, y = q.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if x + dx < 0 or y + dy < 0 or x + dx >= N or y + dy >= M or _map[x + dx][y + dy] > 0:
                continue

            _map[x + dx][y + dy] = 1
            q.append((x + dx, y + dy))

    _sum = 0
    for _m in _map:
        _sum += (len(_m) - sum(_m))
    return _sum
    pass


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empties.append((i, j))
        elif arr[i][j] == 2:
            arr[i][j] = 1
            jags.append((i, j))

for first in range(len(empties)):
    arr[empties[first][0]][empties[first][1]] = 1
    for second in range(first + 1, len(empties)):
        arr[empties[second][0]][empties[second][1]] = 1
        for third in range(second + 1, len(empties)):
            arr[empties[third][0]][empties[third][1]] = 1
            answer = max(answer, bfs())
            arr[empties[third][0]][empties[third][1]] = 0
        arr[empties[second][0]][empties[second][1]] = 0
    arr[empties[first][0]][empties[first][1]] = 0

print(answer)