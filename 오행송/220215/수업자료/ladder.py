def ladder_a():
    for y in range(0, 100):
        for x in range(0, 102):
            if ladder[y][x] == 2:
                if ladder[y-1][x]==1 and ladder[y][x+1]==0 and ladder[y][x-1] ==0:
                    ladder[y-1][x] = 2
                    ladder[y][x] = 1
                    xy = (x,y-1)
                    return xy
                if ladder[y][x + 1] == 1:
                    for k in range(0, len(ladder[y][x:102])):
                        if ladder[y][x:102][k]==0:
                            ladder[y-1][x+k-1] = 2
                            ladder[y][x] = 1
                            xy = (x+k-1,y-1)
                            return xy
                if ladder[y][x -1] == 1:
                    for k in reversed(range(0,len(ladder[y][0:x]))):
                        if ladder[y][0:x][k] == 0:
                            ladder[y-1][k+1] = 2
                            ladder[y][x] = 1
                            xy =(k+1, y-1)
                            return xy

for i in range(0,10):
    T = int(input())
    ladder=[[0]*102 for _ in range(100)]
    for j in range(0,100):
        ladder[j][1:101] = list(map(int,input().split()))

    xy=(150,150)
    Y =(0,0)
    while xy[1] >= 0:
        Y = ladder_a()
        if Y[1] == 0:
            break
    print('#{} {}'.format(T,Y[0]-1))