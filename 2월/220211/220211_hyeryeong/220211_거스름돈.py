# 거스름돈
# 최소 개수로 거슬러 주기

import sys
sys.stdin = open("input_swea1970.txt", "r")

moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for t in range(1, T + 1):
    # 들어오는 돈의 1의 자리는 자르고 구현
    changes = int(input()[:-1] + '0')
    count = [0] * 8

    for m_idx in range(8): # 8은 돈의 length
        if moneys[m_idx] > changes:
            continue
        else:
            count[m_idx] = changes // moneys[m_idx]
            changes -= moneys[m_idx] * count[m_idx]

    print('#{}'.format(t))
    print(*count)



