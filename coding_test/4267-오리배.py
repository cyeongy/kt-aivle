# -*- coding: utf-8 -*-
import sys
from collections import deque

input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [False for _ in range(n + 1)]

q = deque([(s, 0)])

while q:
    cur, idx = q.popleft()
    dp[cur] = True

    # print(">>", cur, idx)
    if cur+v[idx] <= n and not dp[cur + v[idx]]:
        q.append((cur + v[idx], (idx + 1) % m))
        # print(cur+v[idx])

    if cur-v[idx] > 0 and not dp[cur - v[idx]]:
        q.append((cur - v[idx], (idx + 1) % m))
        # print(cur-v[idx])

for idx in range(n, -1, -1):
    if dp[idx]:
        print(idx)
        break
