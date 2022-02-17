import sys
sys.stdin = open("input.txt", "r")


for i in range(0,10):
    T=int(input())
    Nlist=[]
    for j in range(0,100):
        Nlist.append(input())

    Nlist2 = []
    for j in range(0,100):
        NN=''
        for k in range(0,100):
            NN= NN + Nlist[k][j]
        Nlist2.append(NN)


    M = 0
    y = 0
    while M < 100:
        for j in range(0,100):
            for k in range(0,M+1):
                if Nlist[j][k:100-M+k] == Nlist[j][k:100-M+k][::-1]:
                    Y = Nlist[j][k:100-M+k]
                    y = 1

                if Nlist2[j][k:100-M+k] == Nlist2[j][k:100-M+k][::-1]:
                    Y = Nlist2[j][k:100-M+k]
                    y = 1

        if y == 1:
            break
        M += 1
    print('#{} {}'.format(T,len(Y)))
