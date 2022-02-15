T = int(input())

for i in range(0,T):
    box1=[]
    for j in range(0,9):
        box1.append(list(map(int,input().split())))
    good=0
    for y in range(0,9):
        cnt = [0] * 9
        for x in range(0,9):
            cnt[box1[y][x]-1] += 1
        if cnt == [1]*9:
            good += 1


        cnt = [0] * 9
        for x in range(0,9):
            cnt[box1[x][y]-1] += 1
        if cnt == [1] * 9:
            good += 1

    xy=(0,0)
    while 1:
        cnt = [0] * 9
        for y in range(xy[1],xy[1]+3):
           for x in range(xy[0],xy[0]+3):
               cnt[box1[y][x]-1] +=1
        if cnt == [1] * 9:
            good += 1


        if xy[0]==6 and xy[1]==6:
            break
        elif xy[0] < 6:
            xy=(xy[0]+3, xy[1])
        else:
            xy =(0,xy[1]+3)


    if good ==27:
        print('#{} 1'.format(i+1))
    else:
        print('#{} 0'.format(i+1))
