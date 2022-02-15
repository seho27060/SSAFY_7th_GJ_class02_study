T= int(input())

for i in range(0,T):
    N=input()
    Nlist1=[]
    Nlist2=[]
    for j in N:
        Nlist1.append(j)
        Nlist2.append(j)

    max_N=(0,0)
    min_N=(0,9999999999)
    new_N1=''
    new_N2=''
#---------------------------------------------------------------
# 최댓값 최소값 구하기
# 현재 12354 , 10052와 같은 수의 최소값 인식문제
    for j in range(0,len(N)):
        if j==0 and N[0] == '1':
            continue
        if int(N[j]) >= int(max_N[1]):
            max_N= (j,N[j])
        if int(N[j]) <= int(min_N[1]):
            min_N =(j,N[j])
    print(min_N, max_N)
#-----------------------------------------------------------------
# 최댓값 자리바꾸기
    for j in range(0,int(max_N[0])):
        if max_N[1] > N[j]:
            Nlist1[max_N[0]],Nlist1[j]=Nlist1[j],max_N[1]
            break
    for j in Nlist1:
        new_N1= new_N1 + j

#-----------------------------------------------------------------
# 최소값 자리바꾸기

    for j in range(0,min_N[0]):
        if j==0 and N[0] == '1':
            continue
        if min_N[1] < Nlist2[j]:
            Nlist2[min_N[0]] , Nlist2[j] = Nlist2[j] , min_N[1]
            break
    for j in Nlist2:
        new_N2= new_N2 + j


    print('#{} {} {}'.format(i+1,new_N2,new_N1))

