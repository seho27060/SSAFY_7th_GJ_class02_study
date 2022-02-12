### 22. 02. 13. 소수 공부 중



백준 1978

```python
T = int(input())
numbers = map(int, input().split())

cnt = 0
for number in numbers:
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            cnt += 1
            
print(cnt)
```



백준 2581

```python
low = int(input())
high = int(input())

minimum = 1e10
sum_v = 0
for number in range(low, high + 1):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            if minimum > number:
                minimum = number
            sum_v += number

if sum_v == 0: print(-1)
else: print('{}\n{}'.format(sum_v, minimum))
```

신기한 다른 분 코드

```python
import sys
import copy
def f(nums):
    table=nums.copy()
    for i in range(len(table)):
        if table[i] == 1 and i > 1:
            k=i*2
            while(k < len(table)):
                table[k]=0
                k+=i
    
               
    return table
    
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
l=[]
for i in range(max(n, m)+1):
    l.append(1)
    
t=f(l)
exist=0
s=0
minN=max(n, m)
for i in range(min(n, m), max(n, m)+1):
    if t[i] == 1 and i > 1:
        if exist==0:
            exist=1
            
        if minN > i and i > 1:
            minN=i
        
        s+=i
        
if exist == 0:
    print(-1)
else:
    print(s)
    print(minN)
```

