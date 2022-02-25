### BJ 2635 수 이어가기

```python
N = int(input())

# numbers = [N]
longnumbers = []
maxcnt = -1e10

for num in range(1, N + 1):
    numbers = [N] # 여기에서 초기화가 계속 이뤄져야 함
    numbers.append(num)

    idx, cnt = 0, 2
    while True:
        nextnum = numbers[idx] - numbers[idx + 1]
        # val1 = N, val2 = num으로 해놓고
        # val1, val2 = val2, val1 - val2
        # numbers.append(val2)도 가능하네
        if nextnum < 0: break
        numbers.append(nextnum)
        idx += 1
        cnt += 1

    if maxcnt < cnt:
        maxcnt = cnt
        longnumbers = numbers

print(maxcnt)
print(*longnumbers)
```



### BJ 1244 스위치 켜고 끄기

```python
import sys
input = sys.stdin.readline


def Student(lst, num, N): # range를 써도 된다 range(num, N + 1, num)
    newnum = num
    i = 2
    while newnum <= N:
        lst[newnum] = swidic[lst[newnum]]
        newnum = num * i
        i += 1 

def Studentin(lst, num, N):
    left = right = num
    while True:
        if 1 <= left - 1 <= N and 1 <= right + 1 <= N and lst[left - 1] == lst[right + 1]:
            left -= 1
            right += 1
        else: break
    for idx in range(left, right + 1):
        lst[idx] = swidic[lst[idx]]



N = int(input().rstrip()) # 스위치 개수
switches = [-1] + list(map(int, input().rstrip().split()))
# 첫 자리 0이 아니라 -1로 채우자
SN = int(input())

swidic = {0:1, 1:0}

for _ in range(SN):
    stu, num = map(int, input().rstrip().split())
    if stu == 1:
        Student(switches, num, N)
    else:
        Studentin(switches, num, N)
        
cnt = 0
for idx in range(1, N + 1):
    if idx > 20 and (idx - 1) % 20 == 0:
        print()
    print(switches[idx], end=' ')
    cnt += 1

# A = [1, 2, 3, 4, 5, 6]
# del A[0]
# print(A) # [2, 3, 4, 5, 6]

# 아니면
# for idx in range(1, N + 1, 20):
#     print(*swtiches[idx : idx + 20])
```

