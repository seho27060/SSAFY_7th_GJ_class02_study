### 빙글빙글 스네일: 백준 15722



```python
n = int(input())

x = y = 0
cnt = midx = turn = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

multi = []
for i in range(1, n):
    for _ in range(2):
        multi.append(i)
multi = multi + [n - 1]

for s in range(n):
    x += dx[turn]
    y += dy[turn]
    cnt += 1 # 한 번 갔다
    if cnt == multi[midx]:
        turn = (turn + 1) % 4
        midx += 1
        cnt = 0
        
print(x, y)
```

