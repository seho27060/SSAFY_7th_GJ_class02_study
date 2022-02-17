import sys
sys.stdin = open("input.txt", "r")

T= int(input())

for i in range(0,T):
    N,M = map(int, input().split())
    Nlist=[]
    for _ in range(0,N):
        Nlist.append(input())

    Y = ''
    for j in range(0,N):
        nn = ''
        for k in range(0,N):
            if k <= N-M:
                if Nlist[j][k:k+M] == Nlist[j][k:k+M][::-1]:
                    Y = Nlist[j][k:k+M]

    for j in range(0,N-M+1):
        for k in range(0,N):
            nn=''
            for l in range(j,j+M):
                nn = nn + Nlist[l][k]
            if nn == nn[::-1]:
                Y = nn
    print('#{} {}'.format(i + 1,Y))