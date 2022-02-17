T = int(input())

def spin90(A):
    newlist=[]
    for i in range(0,N):
        n =''
        for j in reversed(range(0,N)):
            n += A[j][i]
        newlist.append(n)

    return newlist


for i in range(0,T):
    N = int(input())
    Nlist=[]
    for j in range(0,N):
        Nlist.append(input().split())

    Y = spin90(Nlist)
    Y2 = spin90(Y)
    Y3 = spin90(Y2)

    print('#{}'.format(i+1))
    for j in range(0,N):
        print(Y[j], end=' ')
        print(Y2[j], end=' ')
        print(Y3[j])

