# weekday도 일단 보류

import sys
sys.stdin = open("input_swea_13038.txt", "r")

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    weekdays = list(map(int, input().split()))
    # print(weekdays)

    counts = [0, 0]
    for week in weekdays:
        counts[week] += 1

    new_weekdays = [1] * counts[1]  + [0] * counts[0]

    # print(new_weekdays)

# 일 월 화 수 목 금 토
# a1 a2 a3 a4 a5 a6 a7
# 반드시 일주일에 수업 하나는 열린다
# 교환학생으로 수업을 n번 채워야 한다. n번을 채우기까지 지내야 하는 최소 일수는?

# weekdays sum 구하기

    # week_sum = 0
    # for day in weekdays:
    #     week_sum += day
    # print(week_sum)

    # # 반복문이 두 번 중첩 되었을 때 중간에 완전히 빠져 나오려면 어떻게 해야하지?
    days = 0
    course = 0
    flag = True
    while flag:
        for w in new_weekdays:
            course += w
            days += 1
            if course == n:
                flag = False
                break
    # 처음에 0으로 시작하면 그만큼은 빼줘야 하네 0을 세자

    #
    # vacation = 0
    # for week in weekdays:
    #     if week: break
    #     else: vacation += 1
    #
    # print(vacation)
    # days -= vacation
    # print(days)

    print('#{} {}'.format(t, days))


