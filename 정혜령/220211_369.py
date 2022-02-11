
import sys
sys.stdin = open("input_swea1926.txt", "r")

N = int(input())
for number in range(1, N + 1):
    cnt = 0
    number_copy = number
    for _ in range(number // 10 + 1):
        if number % 10 in (3, 6, 9):
            cnt += 1
        number //= 10
    if cnt > 0: print('-' * cnt, end=' ')
    else: print(number_copy, end=' ')