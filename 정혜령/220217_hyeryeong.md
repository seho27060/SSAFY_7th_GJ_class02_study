### 백만 장자 프로젝트

```python
import sys
sys.stdin = open("input_millionaire.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    # N = 50
    # price = list(map(int, '5902 5728 8537 3857 739 6918 9211 9679 8506 3340 6568 1868 16 7940 6263 4593 1449 6991 310 3355 7068 1431 8580 1757 9218 4934 4328 3676 9355 6221 9080 5922 1545 8511 4067 5467 8674 4691 6504 9835 2034 4965 9980 1221 5895 2501 8152 8325 7731 9302'.split()))

    maxprice = price[-1]
    cnt = bought = sold = 0

    for idx in range(N-2, -1, -1):
        if price[idx] > maxprice:
            sold += maxprice * cnt - bought
            cnt = bought = 0
            maxprice = price[idx]
        else:
            cnt += 1
            bought += price[idx]

    sold += maxprice * cnt - bought

    print('#%d %d' %(t, sold))


```



### 숫자배열회전

```python
# A = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# N = 3

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    new90 = [[-1] * N for _ in range(N)]
    new180 = [[-1] * N for _ in range(N)]
    new270 = [[-1] * N for _ in range(N)]

    # 불필요한 작업이었던 것 같다
    flattenA = []
    for lst in A:
        for val in lst:
            flattenA.append(val)


    # 180, 90
    idx = idx2 = idx3 = 0
    for i in range(N-1, -1, -1): # 180 row, 90 col
        for j in range(N-1, -1, -1): # 180 col
            new180[i][j] = flattenA[idx]
            idx += 1
        for k in range(N): # 90 row
            new90[k][i] = flattenA[idx2]
            idx2 += 1

    # 270
    for l in range(N): #270 col
        for m in range(N-1, -1, -1): #270 row
            new270[m][l] = flattenA[idx3]
            idx3 += 1

    # print(new90, new180, new270)
    for p in range(N):
        print(*new90[p],' ', *new180[p],' ', *new270[p], sep='')
```

