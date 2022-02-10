import sys
sys.stdin = open("input_1204.txt", "r")

T = int(input())
# T = 1 #테스트 용
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    counts = [0] * 101   #점수 범위 0 ~ 100으로 총 101개
    for val in arr:
        counts[val] += 1

    max_v = counts[0]
    num = 0
    max_lst = []
    for idx in range(len(counts)):
        if max_v < counts[idx]:
            max_v = counts[idx]
            num = idx
    for idx in range(len(counts)):
        if max_v == counts[idx]:
            max_lst += [idx]

    real_max = max_lst[0]
    if len(max_lst) > 1:
        for val2 in max_lst:
            if real_max < val2:
                real_max = val2
    print('#{} {}'.format(N, real_max))
