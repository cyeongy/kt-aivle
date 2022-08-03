def electricPay(usage):
    bill = 1600
    if usage <= 100:
        bill += int(usage * 60.7)
    elif usage <= 200:
        bill += int(60.7 * 100 + (usage - 100) * 125.9)
    else:
        bill += int(60.7 * 100 + 100 * 125.9 + (usage - 200) * 187.9)
    
    # tax
    bill = int(1.137 * bill)
    return bill

def practice2(count):
    for i in range(count):
        print('-', end='') if i % 2 else print('+', end='')
    print()


def findCombination(number):
    max_root = number // 2
    answer = []
    for r in range(2, number // 2):
        for p in range(2, 6):
            if number == r ** p:
                answer.append((r, p))
                
    if answer:
        return answer
    else:
        return "No combination"

def gcd(a, b):
    while b != 0:
        n = a % b
        a = b
        b = n
    return a
    

import math

def module_test():
    print(__name__)