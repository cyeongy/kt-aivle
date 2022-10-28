# string = str(input())
#
# for idx in range(len(string)):
#     if int(string[idx]) != 0:
#         answer = int(string[idx])
#         break
#
# for i in range(idx + 1, len(string)):
#     if string[i] == '0':
#         continue
#     answer *= int(string[i])
#
# print(answer)


arr = [(2, False), (3, True), (4, False), (0, True), (1, True), ]

for i in (filter(lambda x: (x[1] and arr.index(x) < 3), arr)):
    print(i)
