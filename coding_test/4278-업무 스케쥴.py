import sys


n = int(input())

arr = []
dp = [0 for _ in range(n+1)]
for _ in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

Max = 0
# print(dp)
for cur, (cost, val) in enumerate(arr):
    # if cur > 0:
    #     print(">>", cur, dp[cur-1])
    #     dp[cur] = dp[cur-1]
    if cur + cost > len(arr):
        continue
    if dp[cur+cost] < val + dp[cur]:
        dp[cur+cost] = val + dp[cur]
        for i in range(cur+cost, n+1):
            # print(dp[i], dp[cur+cost])
            dp[i] = max(dp[i], dp[cur+cost])
    # print(dp)

print(dp[n])
'''
10
3 12
9 7
4 17
4 12
8 28
4 29
4 30
6 18
7 8
1 10

'''

