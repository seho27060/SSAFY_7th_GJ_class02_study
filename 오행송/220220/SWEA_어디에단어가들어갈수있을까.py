T = int(input())

for i in range(T):
    N,K = map(int, input().split())
    Nlist=[]
    for j in range(N):
        Nlist.append(input().split())

    cnt = 0
    for y in range(N):
        for x in range(N-K+1):
            if x == 0:
                if Nlist[y][x:x+K] == ['1']*K and Nlist[y][x+K] != '1':
                    cnt += 1
            if x == N-K:
                if Nlist[y][x:x + K] == ['1']*K and Nlist[y][x-1] != '1':
                    cnt += 1
            else:
                if Nlist[y][x:x + K] == ['1']*K and Nlist[y][x+K] != '1' and Nlist[y][x - 1] != '1':
                    cnt += 1

    for x in range(N):
        for y in range(N-K+1):
            NN = []
            for j in range(y,y+K):
                NN.append(Nlist[j][x])
            if y == 0:
                if NN == ['1']*K and Nlist[y+K][x] != '1':
                    cnt +=1
            elif y == N-K:
                if NN == ['1']*K and Nlist[y-1][x] != '1':
                    cnt += 1
            else:
                if NN == ['1']*K and Nlist[y + K][x] != '1' and Nlist[y-1][x] != '1':
                    cnt += 1

    print('#{} {}'.format(i+1,cnt))