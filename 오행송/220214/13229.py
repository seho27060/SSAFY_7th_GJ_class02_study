day = ['MON', 'TUE','WED','THU','FRI','SAT','SUN']

def move(X):
    temp = X[0]
    for i in range(0,len(X)-1):
        X[i] = X[i + 1]
    X[len(X)-1] = temp
    return X

T = int(input())
for i in range(0,T):
    N = input()
    cnt = 0
    for j in range(0,7):
        if day[0] == N:
            move(day)
            break
        move(day)
    for j in range(0,7):
        cnt += 1
        if day[j] == 'SUN':
            break
    print('#{} {}'.format(i+1,cnt))