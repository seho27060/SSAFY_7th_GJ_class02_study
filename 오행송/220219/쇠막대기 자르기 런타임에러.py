#런타임 에러나서 줄여야함
T= int(input())

for i in range(0,T):
    N = input()

    Nlist=N.replace('()','@')

    Fecnt=0
    for j in range(0,len(Nlist)-1):
        if Nlist[j] == '(':
            cnt =1
            laser = 0
            Fe = 1
            for k in range(j+1,len(Nlist)):
                if Nlist[k] == '(':
                    cnt +=1
                elif Nlist[k] == ')':
                    cnt -=1
                    if cnt == 0:
                        break
                else:
                    laser += 1
            Fe = Fe + laser
            Fecnt += Fe
    print('#{} {}'.format(i+1,Fecnt))