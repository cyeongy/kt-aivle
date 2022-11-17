import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(len(arr))]

dp[0] = 1
for cur in range(1, n):
    for pre in range(cur):
        if arr[pre] <= arr[cur] and dp[pre]+1 > dp[cur]:
            dp[cur] = dp[pre]
        dp[cur] += 1

print(n - max(dp))


'''
nums = [0] + list(map(int,input().split()))
dp = [0, 1]
cp = [0, nums[1]]

for i in range(2, n+1):
    for j in range(len(cp)-1,-1,-1):
        if nums[i] > cp[j]:
            dp.append(j+1)
            if j+1 < len(cp):
                cp[j+1]=nums[i]
            else:
                cp.append(nums[i])
            break
print(n - max(dp))


'''