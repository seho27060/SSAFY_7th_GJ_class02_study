def maxmin():
    max1=(0,0)
    min1=(0,9999999)
    for j in range(0,len(Nlist)):
        if Nlist[j] > max1[1]:
            max1 = (j,Nlist[j])
        if Nlist[j] < min1[1]:
            min1 = (j,Nlist[j])

    if max1[0] > min1[0]:
        Nlist.pop(max1[0])
        Nlist.pop(min1[0])
    else:
        Nlist.pop(min1[0])
        Nlist.pop(max1[0])

    return min1[1],max1[1]




T = int(input())
for i in range(0,T):
    N = int(input())
    Nlist = list(map(int, input().split()))
    newlist =[]
    while 1:
        if len(newlist) == 10:
            break
        if len(Nlist) ==1:
            newlist.append(Nlist[0])
            break
        if len(Nlist) == 0:
            break
        AA = maxmin()

        newlist.append(AA[1])
        newlist.append(AA[0])

    print('#{} {}'.format(i+1,' '.join(map(str,newlist))))