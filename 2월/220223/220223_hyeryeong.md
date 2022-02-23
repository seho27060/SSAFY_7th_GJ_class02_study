###  SWEA 11315. 오목 판정

```python
import sys
sys.stdin = open('input_oomok.txt', 'r')
def IsOmok(board, N, row, col):

    # 가로 찾기
    newr, newc = row, col
    for _ in range(4):
        newc += 1
        if newc == N or board[newr][newc] != 'o':
            break
    else: return True

    # 세로 찾기
    newr, newc = row, col
    for _ in range(4):
        newr += 1
        if newr == N or board[newr][newc] != 'o':
            break
    else: return True

    # 대각선 찾기
    newr, newc = row, col
    for _ in range(4):
        newr += 1
        newc += 1
        if newr == N or newc == N or board[newr][newc] != 'o':
            break
    else: return True

    # 대각선 찾기2
    newr, newc = row, col
    for _ in range(4):
        newr += 1
        newc -= 1
        if newr == N or newc < 0 or board[newr][newc] != 'o':
            break
    else: return True

    return False

# def IsOmok(board, N, row, col):
#     result = False
#
#     # 가로 찾기
#     newr, newc = row, col
#     for _ in range(4):
#         newc += 1
#         if newc == N or board[newr][newc] != 'o':
#             break
#     else: result = True
#
#     # 세로 찾기
#     newr, newc = row, col
#     for _ in range(4):
#         newr += 1
#         if newr == N or board[newr][newc] != 'o':
#             break
#     else: result = True
#
#     # 대각선 찾기
#     newr, newc = row, col
#     for _ in range(4):
#         newr += 1
#         newc += 1
#         if newr == N or newc == N or board[newr][newc] != 'o':
#             break
#     else: result = True
#
#     # 대각선 찾기2
#     newr, newc = row, col
#     for _ in range(4):
#         newr += 1
#         newc -= 1
#         if newr == N or newc < 0 or board[newr][newc] != 'o':
#             break
#     else: result = True
#
#     return result


T = int(input())
# T = 1
for t in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]

    result = 'NO'
    for row in range(N):
        for col in range(N):
            if board[row][col] == 'o' and IsOmok(board, N, row, col):
                result = 'YES'
                break

    print('#{} {}'.format(t, result))
```





### SWEA 1220. Magnetic

```python

import sys
sys.stdin = open('input_magnetic.txt', 'r')

T = 10
# T = 1
for t in range(1, T + 1):
    N = int(input())
    A = [input().split() for _ in range(N)]

    totalcnt = 0
    for col in range(N):
        redcnt = bluecnt = 0
        redblue = []
        for row in range(N):
            if A[row][col] == '1':
                redcnt += 1
                redblue.append('1')
            if A[row][col] == '2':
                bluecnt += 1
                redblue.append('2')
        if redcnt != 0 and bluecnt != 0:
            idx = rbcnt = 0
            while idx < len(redblue):
                if idx + 1 < len(redblue) and redblue[idx] == '1' and redblue[idx + 1] == '2':
                    rbcnt += 1
                    idx += 1
                idx += 1
            totalcnt += rbcnt

    print('#{} {}'.format(t, totalcnt))

```

```python
# 교수님 코드

T = 10
for t in range(1, T + 1):
    N = int(input())
    A = [input().split() for _ in range(N)]

    cnt = 0
    for col in range(N):
        magnetic = False
        for row in range(N):
            # 1 보면 m=True 로 체크하고,
            # m== True인 상태에서 2를 만나면 count 올리고 m = False로 초기화
            if A[row][col] == '1':
                magnetic = True
            elif A[row][col] == '2' and magnetic == True:
                cnt += 1
                magnetic = False

    print('#{} {}'.format(t, cnt))
```

