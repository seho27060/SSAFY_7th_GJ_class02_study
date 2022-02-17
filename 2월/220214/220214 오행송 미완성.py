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
# 최댓값 구하기

    for j in range(0,len(N)):
        if j==0 and N[0] == '1':
            continue
        if int(N[j]) >= int(max_N[1]):
            max_N= (j,N[j])
# -----------------------------------------------------------------
# 현재 12354 , 10052와 같은 수의 최소값 인식문제용
    # for j in range(0,len(N)-1):
    #     if j==0 and N[0] == '1':
    #         continue
    #     if Nlist2[j] > Nlist2[j+1]:
    #         print(j)
    #         if j==0:
    #             for k in range(j+1, len(N)):
    #                 if int(Nlist2[k]) <= int(min_N[1]) and int(Nlist2[k]) > 0:
    #                     min_N =(k,Nlist2[k])
    #             Nlist2[j],Nlist2[min_N[0]] = min_N[1],Nlist2[j]
    #             break
    #         else:
    #             for k in range(j+1, len(N)):
    #                 if int(Nlist2[k]) <= int(min_N[1]):
    #                     min_N =(k,Nlist2[k])
    #             Nlist2[j],Nlist2[min_N[0]] = min_N[1],Nlist2[j]
    #             break

#-----------------------------------------------------------------
    for j in range(0,len(N)):
        if Nlist2 > min(Nlist2[j+1::]):


#-----------------------------------------------------------------
# 최댓값 자리바꾸기
    for j in range(0,int(max_N[0])):
        if max_N[1] > N[j]:
            Nlist1[max_N[0]],Nlist1[j]=Nlist1[j],max_N[1]
            break
#-------------------------------------------------------------------
    for j in Nlist1:
        new_N1= new_N1 + j
    for j in Nlist2:
        new_N2= new_N2 + j

    print('#{} {} {}'.format(i+1,new_N2,new_N1))

