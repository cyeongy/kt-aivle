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
        self.cube = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5 ]
        self.operator = []

    def add_op(self, operator):
        self.operator.append(operator)

    def rotate_util(self, operator):
        C = self.cube
        if operator == 'U':
            C[6], C[7], C[15], C[14] = C[14], C[6], C[7], C[15]
            C[2], C[3], C[8], C[16], C[21], C[20], C[13], C[5] = \
                C[13], C[5], C[2], C[3], C[8], C[16], C[21], C[20]
            # self.cube[0], self.cube[1], self.cube[2], self.cube[3] \
            #     = self.cube[3], self.cube[0], self.cube[1], self.cube[2]
            pass
        elif operator == 'L':
            C[20], C[21], C[23], C[22] = \
                C[22], C[20], C[21], C[23]
            C[12:20] = \
                C[18:20] + C[12:18]
            # self.cube[5], self.cube[1], self.cube[2], self.cube[6] \
            #     = self.cube[1], self.cube[2], self.cube[6], self.cube[5]
            pass
        elif operator == 'F':
            C[8], C[9], C[17], C[16] = \
                C[16], C[8], C[9], C[17]
            C[1], C[3], C[7], C[15], C[21], C[23], C[19], C[11] = \
                C[7], C[15], C[21], C[23], C[19], C[11], C[1], C[3]
            # self.cube[1], self.cube[0], self.cube[4], self.cube[5] \
            #     = self.cube[5], self.cube[1], self.cube[0], self.cube[4]
            pass

    def rotate_point(self, operator):
        if len(operator) == 1:
            self.rotate_util(operator)
        else:
            for _ in range(3):
                self.rotate_util(operator[0])
        print(self.cube)

    def rotate(self):
        answer = 1
        for op in self.operator:
            self.rotate_point(op.upper())

        while self.cube != [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]:
            for op in self.operator:
                self.rotate_point(op.upper())
            print("---")
            answer += 1

        return answer


g = Graph()

n = int(input())
for _ in range(n):
    g.add_op(input())

print(g.rotate())
