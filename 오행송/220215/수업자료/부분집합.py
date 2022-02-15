T = int(input())
for i in range(0,T):
    N,K=map(int, input().split())


    y=0
    for j in range(1<<12):
        cnt = 0
        sum1 = 0
        for k in range(12):
            if j & (1<<k):
                cnt +=1
                sum1 += (k+1)

        if cnt ==N and sum1 ==K:
            y+=1

    print('#{} {}'.format(i+1,y))