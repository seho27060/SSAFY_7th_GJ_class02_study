T = int(input())

for i in range(0,T):
    str1 = input()
    str2 = input()
    cnt = 0
    for j in range(0,len(str2)):
        if str2[j:j+len(str1)] == str1:
            cnt = 1
    print('#{} {}'.format(i+1,cnt))