### 직사각형 BJ 2527



- 시간초과

```python
def rectangle(x, y, p, q):
    rect = []
    for row in range(x, p + 1):
        rect.append((row, y))
        rect.append((row, q))
    for col in range(y, q + 1):
        rect.append((x, col))
        rect.append((p, col))
    return rect       

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    rect1 = rectangle(x1, y1, p1, q1)
    rect2 = rectangle(x2, y2, p2, q2)
    
    cnt = 0
    for i in rect1:
        for j in rect2:
            if i == j:
                cnt += 1
    
    if cnt == 0:
        for i, j in rect2:
            if x1 < i < p1 and y1 < j < q1:
                result = 'a'
                break
        else: result = 'd'
    elif cnt == 1: result = 'c'
    else:
        for i, j in rect2:
            if x1 < i < p1 and y1 < j < q1:
                result = 'a'
                break
        else: result = 'b'
    
    print(result)
    
```

- 뭐가 틀린 건지 알 수가 없다

```python
for _ in range(4): 
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    
    
    if q2 < x1 or x2 > p1: result = 'd'
    elif x2 == x1 or p2 == p1:
        if y2 == q1 or q1 == y1: result = 'b'
        elif y2 > q1 or q2 < y1: result = 'd'
        else: result = 'a'
    elif p2 == x1 or x2 == p1:
        if q2 == y1 or y2 == q1: result = 'c'
        elif q1 < y1 or y2 > q1: result = 'b'
        else: result = 'b'
    else:
        if y2 > q1 or q2 < y1: result = 'd'
        elif q2 == y1 or y2 == q1: result = 'b'
        else: result = 'a'
    
    print(result)
```

```python
for _ in range(4): 
    A, B, C, D, E, F, G, H = map(int, input().split())
    
    if B > H or D < F or G < A or C < E:
        result = 'd'
    elif B == H or E == C or D == F or H == A:
        if (E, F) == (C, D) or (E, H) == (C, B) or\
            (A, B) == (G, H) or (A, D) == (G, F):
            result = 'c'
        else: result = 'b'
    else: result = 'a'
    
    print(result)
```

