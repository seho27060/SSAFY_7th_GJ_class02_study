import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(0,T):
    N,K = map(int,input().split())
    Nlist=[]
    for j in range(0,N):
        Nlist.append(list(map(int,input().split())))

    max1=0
    xy=(0,0)
    while 1:
        cnt = [[0] * K for _ in range(K)]
        sum1=0
        for y in range(xy[1], xy[1] + K):
            for x in range(xy[0], xy[0] + K):
                sum1 = sum1 + Nlist[y][x]
        if sum1 > max1:
            max1 = sum1

        if xy[0] == N-K and xy[1] == N-K:
            break
        elif xy[0] < N-K:
            xy = (xy[0] + 1, xy[1])
        else:
            xy = (0, xy[1] + 1)

    print('#{} {}'.format(i+1,max1))