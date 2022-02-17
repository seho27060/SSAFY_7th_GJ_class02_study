
T = int(input())

for i in range(0,T):
    A,B =input().split()

    cnt=0
    n = 0
    while n < len(A):
        if A[n:n+len(B)] == B:
            cnt += 1
            n += len(B)
        else:
            cnt += 1
            n +=1
    print('#{} {}'.format(i+1,cnt))