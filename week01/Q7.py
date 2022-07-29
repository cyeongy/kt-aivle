# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    pre = None
    for now in arr:
        if pre == now:
            continue
        answer.append(now)
        pre = now
    return answer