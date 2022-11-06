import sys
from collections import defaultdict
from math import gcd


class Solution:
    def __init__(self, n):
        self.N = n
        self.vertices = defaultdict(list)
        self.numbers = [1 for _ in range(n)]
        self.visited = [False for _ in range(n)]

    def addEdge(self, a, b, c, d):
        self.vertices[a].append((b, c, d))
        self.vertices[b].append((a, d, c))

    def solve(self):
        for _ in range(2):
            for a, v in self.vertices.items():
                for b, c, d in v:
                    before_a = self.numbers[a]
                    before_b = self.numbers[b]
                    quotient_a = before_a // gcd(before_a, c)
                    quotient_b = before_b // gcd(before_b, d)
                    self.numbers[a] = c * quotient_a * quotient_b // gcd(quotient_a,
                                                                         quotient_b) // gcd(c,
                                                                                            d)  # // (quotient_a * quotient_b)
                    self.numbers[b] = d * quotient_a * quotient_b // gcd(quotient_a,
                                                                         quotient_b) // gcd(c,
                                                                                            d)  # // (quotient_a * quotient_b)
                    # print(f'vertex: {a, b, c, d}')
                    # print(f'a: {before_a}, {c}->{self.numbers[a]}, {quotient_a}')
                    # print(f'b: {before_b}, {d}->{self.numbers[b]}, {quotient_b}')
                    # print(self.numbers)
        return self.numbers


solution = Solution(4)
arr = [[0, 3, 3, 4],
       [1, 2, 5, 7],
       [2, 3, 3, 4]]
for a, b, c, d in arr:
    solution.addEdge(a, b, c, d)

answer = solution.solve()
print(' '.join(map(str, answer)))


solution = Solution(5)
arr = [[0, 1, 3, 4],
       [1, 2, 5, 8],
       [1, 3, 3, 3],
       [2, 4, 8, 9], ]
for a, b, c, d in arr:
    solution.addEdge(a, b, c, d)

answer = solution.solve()
print(' '.join(map(str, answer)))
