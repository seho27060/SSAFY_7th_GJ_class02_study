import sys
sys.stdin = open("input_1204.txt", "r")

T = int(input())
# T = 1 #테스트 용
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    # 각 숫자가 몇 번 나오는지 counts에 담기
    counts = [0] * 101   #점수 범위 0 ~ 100으로 총 101개
    for val in arr:
        counts[val] += 1
    # print(counts) # 테스트 용
    # counts에서 max 값 찾기
    # max_v = counts[0]
    # num = 0
    # for idx in range(len(counts)):
    #     if max_v < counts[idx]:
    #         max_v = counts[idx]
    #         num = idx
    # print(num, max_v) # 테스트 용
    #
    # # 총 몇 번 등장하는 지
    # cnt = 0
    # max_lst = []
    # for val2 in counts:
    #     if max_v == val2:
    #         cnt += 1
    #         max_lst += [val2]
    # # if cnt > 1:
    # print(max_lst)

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
