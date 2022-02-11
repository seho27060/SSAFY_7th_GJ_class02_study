import sys
sys.stdin = open("input_elecbus.txt", "r")

T = int(input())
# T = 1 # te

for t in range(1, T + 1):

    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))

    distance = stop = cnt = 0
    # 현재 위치, 멈추는 지점, 충전 횟수

    # 검사
    for idx in range(len(charges) - 1):
        if charges[idx + 1] - charges[idx] > K:
            print('#{} 0'.format(t))
            break
    else:

        # bus_line = [0] * (N + 1)
        # for charge in charges:
        #     bus_line[charge] = 1

        while True:
            stop = distance
            distance += K
            if distance >= N:
                break
                # distance가 charges에 없을 때도 가능(in)

            for pos in range(stop, distance + 1):
                # if bus_line[pos]:
                #     max_stop = pos   #방법1 busline이 있는 방법 - 시간이 더 적게 드는데, 메모리는 좀 더 큼
                if pos in charges:     #방법2 busline 없이 가능한 방법 - 시간이 더 오래 걸리는데, 메모리는 좀 더 적음
                    max_stop = pos

            distance = max_stop
            cnt += 1

        print('#{} {}'.format(t, cnt))