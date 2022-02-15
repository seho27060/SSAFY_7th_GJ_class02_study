T = int(input())
for k in range(0,T):

    N = int(input())
    arr= [[0]*N for _ in range(N)]

    a= 0
    n=1
    A = N
    while 1:
        for i in range(a,a+1):
          for j in range(a,A):
                arr[i][j] = n
        if n > N**2:
            break
        for i in range(a+1,A):
            for j in range(A-1,A):
                arr[i][j] = n
                n += 1
                if n > N ** 2:
                    break
        if n > N**2:
            break
        for i in range(A-1,A):
            for j in reversed(range(a,A-1)):
                arr[i][j] = n
                n += 1
        if n > N**2:
            break
        for i in reversed(range(a+1,A-1)):
            for j in range(a,a+1):
                arr[i][j] = n
                n += 1
        if n > N ** 2:
            break
        a += 1
        A -=1

    print('#{}'.format(k+1))
    for l in arr:
        print('{}'.format(' '.join(map(str,l))))