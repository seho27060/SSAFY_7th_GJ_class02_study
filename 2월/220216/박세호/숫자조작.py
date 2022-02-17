nums = int(input())

for i in range(nums):
    lst = list(input())     # 입력 데이터를 str으로 구성된 list 로 뱓음

    get_ = set()            # 효율적 정리를 위한 set 선언
    get_.add(int("".join(lst)))         # 아무것도 바꾸지 얺는 경우를 사전에 추가.
    for j in range(len(lst)):           # 1번째 수부터 n번째 수까지 순회하며 모든 자리의 수와 바꾸는 이중 포문
        for k in range(len(lst)):
            if j != k:                  # 같은 자리의 숫자는 바꿀수 없으므로 조건으로 배제
                get_lst = lst.copy()    # 원 리스트를 복사해주고,
                get_lst[j],get_lst[k] = get_lst[k],get_lst[j]   #j번째 자리 숫자와 k번째 자리 숫자를 바꿔준다.
                if get_lst[0] != "0":                           # 바꾼 값 get_lst의 첫번째 값이 0 이 아니라면,
                    get_.add(int("".join(get_lst)))             # get_ 에 int 형태로 추가해준다.
    print("#{0} {1} {2}".format(i+1,min(get_),max(get_)))      # get_에서 최대 최소 값을 출력한다.


