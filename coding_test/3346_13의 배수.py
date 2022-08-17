# -*- coding: utf-8 -*-
import sys

N = sys.stdin.readline().rstrip()
end = 10 ** (len(N))
elements = list(N)


answer = []

visited = [False] * len(N)
now = ['_'] * len(N)

def perm(idx):
    if idx == len(N):
        temp = int(''.join(now))
        answer.append(temp % 13 == 0)
    else:
        for i in range(len(N)):
            if visited[i]:
                continue
            visited[i] = True
            now[idx] = elements[i]
            perm(idx+1)
            visited[i] = False

perm(0)

print(True in answer)