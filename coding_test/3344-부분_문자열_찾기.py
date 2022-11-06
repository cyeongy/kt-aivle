import re

query = 'tawerqccbc'
target = 'abtc'

A = query
B = target

answer = "NO"

idx = 0

for a in A:
    print(a, B[idx])

    if B[idx] == a:
        idx += 1
    if idx >= len(B):
        answer = "YES"


print(answer)p