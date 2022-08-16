import sys
from decimal import Decimal
from fractions import Fraction

a = '0.31984'

print(a[2:])
print(len(a))

#
# temp = [1, 3, 5, 7]
#
# print(temp.index(3))
#
# colors = {
#     'R': (1, 0, 0),
#     'G': (0, 1, 0),
#     'B': (0, 0, 1),
#     (1, 0, 0): 'R',
#     (0, 1, 0): 'G',
#     (0, 0, 1): 'B',
#     (1, 1, 0): 'Y',
#     (0, 1, 1): 'C',
#     (1, 0, 1): 'M',
# }
#
#
# def add(ref1, ref2):
#     return tuple(1 if lhs + rhs > 0 else 0 for lhs, rhs in zip(ref1, ref2))
#
#
# N, M = map(int, sys.stdin.readline().split())
#
# arr = [[(1, 1, 0)] * M for _ in range(N)]
#
# arr[0][0] = add(arr[0][0], (0, 2, 0))
#
# print(arr)
#
