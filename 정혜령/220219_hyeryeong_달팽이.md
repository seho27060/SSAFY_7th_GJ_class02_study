# 달팽이

### 달팽이 Baekjoon 1913

- (0, 0)에서 시작하기

```python
def spiralorder(N, num):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    
    numbers = [i for i in range(N * N, -1, -1)]
    snail = [[0] * N for _ in range(N)]
    r = c = 0
    box = turn = 0
    
    while box < N * N:
        snail[r][c] = numbers[box]
        if numbers[box] == num:
            numr, numc = r + 1, c + 1
        box += 1
        tempr = r + dr[turn]
        tempc = c + dc[turn]
        if tempr < 0 or tempr == N or tempc < 0 or tempc == N or snail[tempr][tempc]:
            turn = (turn + 1) % 4
        r += dr[turn]
        c += dc[turn]
    
    return snail, numr, numc

N = int(input())
num = int(input())
matrix, x, y = spiralorder(N, num)
for lst in matrix:
    print(*lst)
print(x, y)
```

- 중앙에서 시작하기

```python
def spiralorder(N, num): # 자연수 N, 좌표 찾을 num
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    numbers = [i for i in range(1, N * N + 1)]
    snail = [[0] * N for _ in range(N)]
    
    multi = []
    for i in range(1, N):
        for _ in range(2):
            multi.append(i)
    multi = multi + [N]
    
    r = c = N // 2
    midx = box = 0
    turn = 0
    
    while box < N * N - (N - 1): # multi 때문에 한 번에 작용하니까
        for _ in range(multi[midx]):
            snail[r][c] = numbers[box]
            if numbers[box] == num:
                targetr = r + 1
                targetc = c + 1
            box += 1
            r += dr[turn]
            c += dc[turn]
        turn = (turn + 1) % 4
        midx += 1
        
    return snail, targetr, targetc

# print(spiralorder(7))

N = int(input())
num = int(input())
matrix, x, y = spiralorder(N, num)
for lst in matrix:
    print(*lst)
print(x, y)
```



### 달팽이2 Baekjoon 1952

- 달팽이 방향 전환 수 세기

```python
M, N = map(int, input().split())

matrix = [[0] * N for _ in range(M)]
r = c = box = turn = turncnt = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while box < N * M:
    matrix[r][c] = 1
    box += 1
    newr = r + dr[turn]
    newc = c + dc[turn]
    if newr < 0 or newr == M or newc < 0 or newc == N or matrix[newr][newc]:
        turn = (turn + 1) % 4
        turncnt += 1
    r += dr[turn]
    c += dc[turn]

print(turncnt - 1)
```



### 달팽이3 Baekjoon 1959

- 달팽이 방향전환 횟수, 마지막 지점 좌표 구하기

```python
M, N = map(int, input().split())

top, bottom, left, right = 0, M, 0, N

# turn 구하기
if M <= N:
    turn = 2 * (M - 1)
else:
    turn = 2 * N - 1

# 마지막 지점 좌표 구하기
mok, nameoji = divmod(turn, 4)

if nameoji == 0:
    top += mok; bottom -= mok; right -= mok; left += mok
    r = bottom; c = right 
elif nameoji == 1:
    top = top + mok + 1; bottom -= mok; right -= mok; left += mok
    r = bottom; c = right 
elif nameoji == 2:
    top = top + mok + 1; bottom -= mok; right = right - mok -1; left += mok
    r = bottom; c = left + 1 
else:
    top = top + mok + 1; bottom = bottom - mok -1
    right = right - mok -1; left += mok
    r = top + 1; c = right

print(turn)
print(r, c)
```

