T = int(input())

for i in range(0,T):
    str1 = input()
    str2 = input()

    maxcnt=0
    for j in str1:
        cnt = 0
        for k in str2:
            if j == k:
                cnt += 1
        if cnt > maxcnt:
            maxcnt = cnt
    print('#{} {}'.format(i+1,maxcnt))