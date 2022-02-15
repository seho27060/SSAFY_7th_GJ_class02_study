def dlwlstn(X):
    if X == 0:
        return '0'
    if X ==1:
        return '1'
    elif X%2 ==1:
        return dlwlstn(X//2)+'1'
    else:
        return dlwlstn(X//2)+'0'


T=int(input())

for i in range(0,T):

    N,M= map(int,input().split())
    NN = dlwlstn(M)
    if len(NN) >= N:
        if str(NN[-1:-N-1:-1]) == '1'*N:
            print('#{} ON'.format(i + 1))
        else:
            print('#{} OFF'.format(i + 1))
    else:
        print('#{} OFF'.format(i+1))


