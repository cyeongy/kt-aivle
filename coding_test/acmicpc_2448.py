N = int(input())

star = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]


def recursive(n, before):
    answer = [[' ' for _ in range(4 * n - 1)] for _ in range(2*n)]
    for i in range(n):
        answer[i][n:] = before[i]
        pass

    for t_row, row in enumerate(range(n, 2 * n)):
        answer[row][:2 * n] = before[t_row]
        answer[row][2 * n:] = before[t_row]

    if 2 * n == N:
        return answer

    return recursive(2 * n, answer)


if N == 3:
    answer = star
else:
    answer = recursive(3, star)

for i in range(N):
    print(''.join(answer[i]))
