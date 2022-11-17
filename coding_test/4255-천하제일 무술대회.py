import sys

n = int(input())
dp = []
for _ in range(n):
    a, b = sys.stdin.readline().strip().split()
    b = int(b)

    dp.append((b, a))

winner = max(dp, key=lambda x: x[0])
while n > 1:
    reindex = 0
    for idx in range(0, n, 2):
        if dp[idx] == winner:
            print(dp[idx+1][1])
        elif dp[idx+1] == winner:
            print(dp[idx][1])
        dp[reindex] = max(dp[idx], dp[idx+1], key=lambda x: x[0])
        reindex += 1

    n = n // 2


