import sys

sys.setrecursionlimit(int(10e5))

'''
    2   3
1   0

    6   7
5   4


        0   1
        2   3
4   5   6   7   8   9   10  11
12  13  14  15  16  17  18  19
        20  21
        22  23


'''


class Graph:
    def __init__(self):
        self.cube = list(range(24))
        self.edge = list(range(8))
        self.operator = []

    def add_op(self, operator):
        self.operator.append(operator)

    def rotate_util(self, operator):
        C = self.cube
        E = self.edge
        if operator == 'U':
            C[6], C[7], C[15], C[14] = C[14], C[6], C[7], C[15]
            C[2], C[3], C[8], C[16], C[21], C[20], C[13], C[5] = \
                C[13], C[5], C[2], C[3], C[8], C[16], C[21], C[20]
            E[0], E[1], E[2], E[3] \
                = E[3], E[0], E[1], E[2]
            pass
        elif operator == 'L':
            C[20], C[21], C[23], C[22] = \
                C[22], C[20], C[21], C[23]
            C[12:20] = \
                C[18:20] + C[12:18]
            E[5], E[1], E[2], E[6] \
                = E[1], E[2], E[6], E[5]
            pass
        elif operator == 'F':
            C[8], C[9], C[17], C[16] = \
                C[16], C[8], C[9], C[17]
            C[1], C[3], C[7], C[15], C[21], C[23], C[19], C[11] = \
                C[7], C[15], C[21], C[23], C[19], C[11], C[1], C[3]
            E[1], E[0], E[4], E[5] \
                = E[5], E[1], E[0], E[4]
            pass

    def rotate_point(self, operator):
        if len(operator) == 1:
            self.rotate_util(operator)
        else:
            for _ in range(3):
                self.rotate_util(operator[0])
        print(self.cube, '\t', self.edge)

    def rotate(self):
        answer = 1
        for op in self.operator:
            self.rotate_point(op.upper())
        while self.cube != list(range(24)) or self.edge != list(range(8)):
            for op in self.operator:
                self.rotate_point(op.upper())
            # print("---")
            answer += 1

        return answer


g = Graph()

n = int(input())
for _ in range(n):
    g.add_op(input())

print(g.rotate())
# print(4)


# # -*- coding: utf-8 -*-
# import sys
#
#
# def display_cube():
#     for i in cube:
#         print(i)
#     print()
#
#
# inputs = []
# for i in range(int(sys.stdin.readline())):
#     inputs.append(sys.stdin.readline().strip())
#
#
# def make_cube():
#     temp = [["w"] * 8 for i in range(2)]
#     for i in range(2):
#         temp.append(["o", "o", "g", "g", "r", "r", "b", "b"])
#     temp.extend([["y"] * 8 for i in range(2)])
#     return temp
#
#
# temp = make_cube()
# cube = make_cube()
#
#
# def up(reverse=False):
#     if not reverse:
#         a, b, c, d, e, f, g, h = cube[2]
#         for i in range(0, 6, 2):
#             cube[2][i] = cube[2][i + 2]
#             cube[2][i + 1] = cube[2][i + 3]
#         cube[2][6], cube[2][7] = a, b
#         cube[0][2], cube[0][3], cube[1][3], cube[1][2] = cube[1][2], cube[0][2], cube[0][3], cube[1][3]
#
#     else:
#         a, b, c, d, e, f, g, h = cube[2]
#         for i in range(7, 2, -2):
#             cube[2][i] = cube[2][i - 2]
#             cube[2][i - 1] = cube[2][i - 3]
#         cube[2][0], cube[2][1] = g, h
#         cube[0][2], cube[0][3], cube[1][3], cube[1][2] = cube[0][3], cube[1][3], cube[1][2], cube[0][2]
#
#
# def left(reverse=False):
#     lists = []
#
#     for i in range(6):
#         lists.append(cube[i][2])
#     lists.append(cube[2][7])
#     lists.append(cube[3][7])
#
#     a, b, c, d, e, f, g, h = lists
#     if reverse:
#         for i in range(0, 4, 2):
#             cube[i][2] = cube[i + 2][2]
#             cube[i + 1][2] = cube[i + 3][2]
#         cube[4][2], cube[5][2] = cube[3][7], cube[2][7]
#         cube[3][7], cube[2][7] = a, b
#         cube[2][0], cube[2][1], cube[3][1], cube[3][0] = cube[2][1], cube[3][1], cube[3][0], cube[2][0]
#     else:
#         for i in range(5, 2, -2):
#             cube[i][2] = cube[i - 2][2]
#             cube[i - 1][2] = cube[i - 3][2]
#         cube[0][2], cube[1][2] = cube[3][7], cube[2][7]
#         cube[3][7], cube[2][7] = e, f
#
#         cube[2][0], cube[2][1], cube[3][1], cube[3][0] = cube[3][0], cube[2][0], cube[2][1], cube[3][1]
#
#
# def front(reverse=False):
#     if reverse:
#         a, b = cube[3][1], cube[2][1]
#         c, d = cube[1][2], cube[1][3]
#         e, f = cube[2][4], cube[3][4]
#         g, h = cube[4][3], cube[4][2]
#
#         cube[3][1], cube[2][1] = c, d
#         cube[1][2], cube[1][3] = e, f
#         cube[2][4], cube[3][4] = g, h
#         cube[4][3], cube[4][2] = a, b
#         cube[2][2], cube[2][3], cube[3][3], cube[3][2] = cube[2][3], cube[3][3], cube[3][2], cube[2][2]
#     else:
#         a, b = cube[3][1], cube[2][1]
#         c, d = cube[1][2], cube[1][3]
#         e, f = cube[2][4], cube[3][4]
#         g, h = cube[4][3], cube[4][2]
#
#         cube[3][1], cube[2][1] = g, h
#         cube[1][2], cube[1][3] = a, b
#         cube[2][4], cube[3][4] = c, d
#         cube[4][3], cube[4][2] = e, f
#
#         cube[2][2], cube[2][3], cube[3][3], cube[3][2] = cube[3][2], cube[2][2], cube[2][3], cube[3][3]
#
#
# count = 0
#
# while True:
#     for command in inputs:
#         if command == "U":
#             up()
#         elif command == "U0":
#             up(True)
#         elif command == "L":
#             left()
#         elif command == "L0":
#             left(True)
#         elif command == "F":
#             front()
#         elif command == "F0":
#             front(True)
#     count += 1
#     if temp == cube:
#         print(count)
#         break
