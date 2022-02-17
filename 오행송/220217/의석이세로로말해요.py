T = int(input())

for i in range(0,T):
    Nlist = []
    N = ''
    for j in range(0,5):
        Nlist.append(str(input()))


    for k in range(0,15):
        for j in range(0,5):
            N += Nlist[j][k:k+1]

    print('#{} {}'.format(i+1, N))
