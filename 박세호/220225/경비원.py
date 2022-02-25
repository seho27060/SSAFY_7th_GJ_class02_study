w,h = map(int,input().split())
nums = int(input())
lst = [list(map(int,input().split())) for i in range(nums)] ## 상점 위치

now_ = list(map(int,input().split()))                       ## 현재 내 위치
around = 2*(w+h)                                            ## 조건 확인을 위한 둘레 길이
answer = 0              ## 출력을 위한 변수 초기화
for j in lst:           ## 입력값 순회
    get_ = 0            ## 각 입력값의 최소값 산출을 위한 초기화
    if now_[0] == 1:    ## 내가 북쪽 경계에 있다면.
        if j[0] == 1:   ## 상점이 같은 경계에 있을시,
            get_ = abs(now_[1] - j[1])      ## 차이의 절댓값 산출.
        elif j[0] == 2: ## 상점이 남쪽에 있을 시,
            get_ = now_[1] + j[1] + h       ## 두가지 길중 1개 산출
        elif j[0] == 3: ## 서쪽에 있을시,
            get_ = now_[1] + j[1]           ## 두가지 길중 1개 산출
        elif j[0] == 4: ## 동쪽에 있을시,
            get_ = (w-now_[1]) + j[1]       ## 두가지 길 중 1개 산출.
    elif now_[0] == 2:  ## 내가 남 서 동에 있을때, 위 하위 조건과 비슷하게 판별.
        if j[0] == 1:
            get_ = now_[1] + j[1] + h
        elif j[0] == 2:
            get_ = abs(now_[1] - j[1])
        elif j[0] == 3:
            get_ = now_[1] + (h-j[1])
        elif j[0] == 4:
            get_ = (w - now_[1]) + (h-j[1])
    elif now_[0] == 3:
        if j[0] == 1:
            get_ = now_[1] + j[1]
        elif j[0] == 2:
            get_ = (h-now_[1]) + j[1]
        elif j[0] == 3:
            get_ = abs(now_[1] - j[1])
        elif j[0] == 4:
            get_ = now_[1] + w + j[1]
    elif now_[0] == 4:
        if j[0] == 1:
            get_ = now_[1] + (w-j[1])
        elif j[0] == 2:
            get_ = (h-now_[1]) + (w-j[1])
        elif j[0] == 3:
            get_ = now_[1] + w + j[1]
        elif j[0] == 4:
            get_ = abs(now_[1] - j[1])
    get_ = abs(get_)    ## 1차적으로 값 산출.
    if get_ > abs(around - get_):   ## 이동 경로는 반시계, 시계 방향 둘중 하나고,
        get_ = abs(around - get_)   ## 두개 값의 합은 둘레이므로, 이를 활용하여 최솟값 산출.

    answer += get_                  ## 총합 구하기.
print(answer)

