T = int(input())

for i in range(0,T):
    P,A,B = map(int,input().split())

    cnta=0
    p1 = P
    l1=1
    while 1:
        cnta +=1
        if (p1+l1)//2 == A:
            break
        if (p1+l1)//2 < A:
            l1 = (p1+l1)//2
        else:
            p1= (p1+l1)//2

    cntb=0
    p2 = P
    l2=1
    while 1:
        cntb +=1
        if (p2+l2)//2 == B:
            break
        if (p2+l2)//2 < B:
            l2 = (p2+l2)//2
        else:
            p2= (p2+l2)//2
    print(cnta,cntb)
    if cnta < cntb:
        print('#{} A'.format(i+1))
    elif cnta > cntb:
        print('#{} B'.format(i + 1))
    else:
        print('#{} 0'.format(i + 1))