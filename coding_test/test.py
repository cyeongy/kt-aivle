import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
import copy

# x = np.linspace(0, 1, 50)
# p1 = np.power(x, 2)
# p2 = np.power(1-x, 2)
#
# plt.plot(x, 1-p1-p2)
# plt.xlabel('P_i')
# plt.ylabel('Gini Index')
# plt.grid()
# plt.xlim(0, 1)
# plt.xticks([0.1 * i for i in range(11)])
#
# plt.axvline(.5, color='red')
# plt.axvline(.48, color='green')
# plt.axvline(.176, color='purple')
# plt.show()

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

bandwidth = {0: [0, 1], 1: [0, 1, 2], 2: [1, 2]}

Max = [[0, 0, 0], [0, 0, 0]]
Min = [[0, 0, 0], [0, 0, 0]]

for i in range(3):
    Max[0][i] = arr[0][i]
    Min[0][i] = arr[0][i]

Max[0] = copy.deepcopy(arr[0])
Min[0] = copy.deepcopy(arr[0])

for depth in range(1, N):
    for i in range(3):
        Max[1][i] = arr[depth][i]
        Min[1][i] = arr[depth][i]
    for idx in range(3):
        Max[1][idx] += max(list(Max[0][b] for b in bandwidth[idx]))
        Min[1][idx] += min(list(Min[0][b] for b in bandwidth[idx]))
        pass
    for i in range(3):
        Max[0][i] = Max[1][i]
        Min[0][i] = Min[1][i]

print(max(Max[1]), min(Min[1]))
