T = int(input())

for i in range(0,T):
    arr = [[0]*10 for _ in range(10)]

    N = int(input())
    for j in range(0,N):
        x1,y1,x2,y2,c = map(int,input().split())
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                if arr[y][x] != 0 and arr[y][x] != c:
                    arr[y][x] = 3
                else:
                    arr[y][x] = c

    cnt=0
    for y in range(0,10):
        for x in range(0, 10):
            if arr[y][x] == 3:
                cnt +=1
    print('#{} {}'.format(i+1,cnt))

