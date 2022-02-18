### 백준 2116 주사위 쌓기

```python
import sys

# 현재 상하면 index로 주사위 옆면 max값 찾는 함수
def findmax(dice, currI):
    maxV = 0
    if currI == 0 or currI == 5:
        for i in (1, 2, 3, 4):
            if maxV < dice[i]:
                maxV = dice[i]
    elif currI == 2 or currI == 4:
        for i in (0, 1, 3, 5):
            if maxV < dice[i]:
                maxV = dice[i]
    else:
        for i in (0, 2, 4, 5):
            if maxV < dice[i]:
                maxV = dice[i]
    return maxV

# 전 주사위 윗면 값(preV)으로
# 현재 주사위의 윗면 index와 현재 윗면 값(currV)을 찾아내는 함수
def findidx(dice, preV): 
    for i in range(6):
        if dice[i] == preV:
            if i == 0: currI = 5; currV = dice[5]
            elif i == 1: currI = 3; currV = dice[3]
            elif i == 2: currI = 4; currV = dice[4]
            elif i == 3: currI = 1; currV = dice[1]
            elif i == 4: currI = 2; currV = dice[2]
            elif i == 5: currI = 0; currV = dice[0]
    return currI, currV


# 주사위 개수
N = int(sys.stdin.readline().rstrip())
dice = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

maxsum = 0
for i in range(6):  # 주사위 첫 면 index 0 ~ 5일 때
    currI = i
    currV = dice[0][i]
    numsum = findmax(dice[0], currI)
    for di in range(1, N):              #전 주사위의 값
        currI, currV = findidx(dice[di], currV)
        # 현 주사위 index, 현 주사위 윗면 값
        numsum += findmax(dice[di], currI)
    if maxsum < numsum:
        maxsum = numsum
print(maxsum)
```

