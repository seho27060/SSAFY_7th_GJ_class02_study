# 코드 후반부 그냥 폐기하고 처음부터 만들어야 할듯
# 실패

import sys
sys.stdin = open("input_swea1244.txt", "r")

T = int(input())
T = 1

for t in range(1, T + 1):
    numbers, changes = input().split()
    numbers, changes = '2737', '1'

    # 숫자 리스트에 넣기 
    original_number = []
    number_count = [0] * 10 # 0 ~ 10
    numbering = 0

    for number in numbers:
        original_number += [int(number)]
        # original_number += [[numbering, int(number)]]
        number_count[int(number)] += 1
        numbering += 1


    # descending order
    number_desc = []
    for num in range(len(number_count) - 1, -1, -1):
        if number_count[num] != 0:
            number_desc += [num] * number_count[num]


    c = 0
    # c_idx = len(number_count) - 1 # count 마지막 지점 idx
    o_idx = 0        # original_number idx
    while c < int(changes):

        if original_number == number_desc:
            if int(changes) - c:
                # original_number[-2][1], original_number[-1][1] = original_number[-1][1], original_number[-2][1]
                original_number[-2], original_number[-1] = original_number[-1], original_number[-2]
            break

        #else
        # number count 거꾸로 가기
        for idx in range(len(number_count) - 1, -1, -1): # idx가 max값
            if number_count[idx]:
                for idx2 in range(len(original_number)): # original number의 자릿수
                    if idx == original_number[o_idx]:
                    # if idx == original_number[o_idx][1]:
                        o_idx += 1
                        continue
                    else:
                        for i in range(o_idx, len(original_number)):
                            if original_number[i] == idx: # max 값과 같은 originalnumber의 숫자
                                for j in range(o_idx + 1, len(original_number)):
                                    if original_number[j] == idx:
                                        number_count[idx] -= 1
                                        original_number[j] = original_number[o_idx]
                                        original_number[o_idx] = idx
                                        break


        c += 1

    print(original_number)









