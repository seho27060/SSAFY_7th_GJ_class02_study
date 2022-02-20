T = int(input())

for i in range(T):
    N = input()
    Nlist = N.replace('()', '@')
    fe = 0
    fecnt =0
    print(Nlist)
    for j in Nlist:
        if j == '(':
            fe += 1
        if j == ')':
            fe -= 1
            fecnt += 1
        if j == '@':
            fecnt += fe
    print('#{} {}'.format(i+1,fecnt))