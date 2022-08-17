import sys

N = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())

sign = 1 if x >= 0 else -1

x *= sign

sub = []

for a in range(x + 1):
    i = (N ** 2) + (a ** 2)
    j = (y ** 2) + ((x - a) ** 2)
    temp = i ** (1/2) + 2 * (j**(1/2))
    sub.append(temp)

print(sign * sub.index(min(sub)))
