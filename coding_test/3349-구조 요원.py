import sys

N = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())

sign = 1 if x >= 0 else -1

x *= sign

sub = []

for a in range(x + 1):
    temp = ((N ** 2) + (a ** 2)) + (((x - a) ** 2) + (y ** 2)) * 4
    print(a, temp)