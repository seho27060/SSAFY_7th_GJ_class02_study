### BJ 10870 피보나치 수 5

```python
def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)


N = int(input())
print(fibo(N))
```



### BJ 1003 피보나치 함수

```python
# 첫 번째 방법 -> 시간초과날 거 같아서 시도 안 함
def fibo(n):
    global memo, cnt1, cnt0
    if n == 0: cnt0 += 1
    if n == 1: cnt1 += 1
    if n >= 2 and memo[n] == -1:
        memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

memo = [-1] * 41
memo[0], memo[1] = 0, 1

T = int(input())
for _ in range(T):
    cnt0 = cnt1 = 0
    N = int(input())
    F = fibo(N)
    print(F, cnt0, cnt1)

# 두 번째 방법 -> 카운트만 계산해도 역시 시간초과
# 사실 위랑 동일
def fibo(n):
    global cnt0, cnt1
    if n == 0:
        cnt0 += 1
        return 0
    if n == 1:
        cnt1 += 1
        return 1
    return fibo(n - 1) + fibo(n - 2)

T = int(input())
for _ in range(T):
    cnt0 = cnt1 = 0
    N = int(input())
    F = fibo(N)
    print(cnt0, cnt1)
    
# 세 번째 방법 -> 0 과 1도 피보나치로 증가한다는 것을 발견
def fibocnt0(N):
    global cnt0
    if N >= 2 and cnt0[N] == -1:
        cnt0[N] = fibocnt0(N - 1) + fibocnt0(N - 2)
    return cnt0[N]

def fibocnt1(N):
    global cnt1
    if N >= 2 and cnt1[N] == -1:
        cnt1[N] = fibocnt1(N - 1) + fibocnt1(N - 2)
    return cnt1[N]

cnt0 = [1, 0] + [-1] * 39
cnt1 = [0, 1] + [-1] * 39

T = int(input())
for _ in range(T):
    N = int(input())
    print(fibocnt0(N), fibocnt1(N))

# 네 번째: 세 번째를 좀 더 하나의 식으로 줄여보기
def fibocnt(N):
    global cnt
    if N >= 2 and cnt[N] == -1:
        cnt[N] = fibocnt(N - 1) + fibocnt(N - 2)
    return cnt[N]

cnt = [0, 1] + [-1] * 39

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0: A, B = 1, 0
    else: A, B = fibocnt(N - 1), fibocnt(N)

    print(A, B)
```



### BJ 9461 파도반 수열

```python
def triangle(N):
    if N > 5 and memo[N] == 0:
        memo[N] = triangle(N - 5) + triangle(N - 1)
    return memo[N]

memo = [0] * 101
memo[1] = memo[2] = memo[3] = 1
memo[4] = memo[5] = 2

T = int(input())

for _ in range(T):
    N = int(input())
    print(triangle(N))
```





### SWEA 진기의 붕어빵

```python

# 시간 초과

T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()

    fishbread = idx = 0
    sec = 1
    while idx < N:
        if sec % M == 0:
            fishbread += K
        if sec == customer[idx]:
            fishbread -= 1
            if fishbread < 0:
                print('#{} Impossible'.format(t))
                break
            idx += 1
        sec += 1
    else: print('#{} Possible'.format(t))

# 풀이 2
T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()


    for idx in range(N):
        sec = customer[idx]
        fishbread = (sec // M) * K
        peoplecnt = idx + 1
        if fishbread - peoplecnt < 0:
            print('#{} Impossible'.format(t))
            break
    else: print('#{} Possible'.format(t))
```





### 기지국

```python
T = int(input())

D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
repeat = {'A': 1, 'B': 2, 'C': 3}
for t in range(1, T + 1):
    N = int(input())
    land = [list(input()) for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if land[row][col] == 'A' or land[row][col] == 'B' or\
                land[row][col] == 'C':
                for dr, dc in D:
                    for i in range(1, repeat[land[row][col]] + 1):
                        newR = row + dr * i
                        newC = col + dc * i
                        if 0 <= newR < N and 0<= newC < N and\
                            land[newR][newC] == 'H':
                            land[newR][newC] = 'X'

    cnt = 0
    for row in range(N):
        for col in range(N):
            if land[row][col] == 'H':
                cnt += 1

    print('#{} {}'.format(t, cnt))
```



