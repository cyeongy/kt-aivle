string = str(input())


for idx in range(len(string)):
    if int(string[idx]) != 0:
        answer = int(string[idx])
        break

for i in range(idx + 1, len(string)):
    if string[i] == '0':
        continue
    answer *= int(string[i])

print(answer)
    


