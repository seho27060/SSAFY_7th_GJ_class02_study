### SWEA 13428. 숫자조작

```python
T = int(input())
 
for t in range(1, T + 1):
 
    strV = input()
    number = int(strV)
    numbers = list(map(int, strV))
 
    maxV = minV = number
 
    for idx in range(len(numbers)):
        for idx2 in range(idx, len(numbers)):
            changed = numbers[::]
            if idx != idx2:
                changed[idx], changed[idx2] = changed[idx2], changed[idx]
                if changed[0] != 0:
                    newnum = 0
                    for idx3 in range(len(changed)):
                        newnum += 10 ** idx3 * changed[len(changed) -1 - idx3]
                    if maxV < newnum:
                        maxV = newnum
                    if minV > newnum:
                        minV = newnum
 
    print('#{} {} {}'.format(t, minV, maxV))
```





### SWEA. 1244 최대상금

- 못 풀었지만 올립니다...

```python
# 최대 상금

# 숫자 최대 6자리, 최대 교환 횟수 10번

# 32888 두 번 교환할 때
# 1 번만 하면 그냥 max값을 앞으로 가져온 82883
# 2번을 하면 88823이 아니라 88832가 되어야 한다는게..

numbers = [3, 2, 8, 8, 8]
totalchange = 2

sortednumbers = sorted(numbers, reverse=True)
print(sortednumbers)

def findmax(lst, currentPos):
    maxPos = currentPos
    for newidx in range(currentPos, len(lst)):
        if lst[maxPos] <= lst[newidx]:
            maxPos = newidx
    return maxPos

cnt = idx = 0

while cnt <= totalchange and idx < len(numbers):
    maxPos = findmax(numbers, idx)
    if numbers[idx] != numbers[maxPos]:
        numbers[idx], numbers[maxPos] = numbers[maxPos], numbers[idx]
        cnt += 1
        idx += 1
    else:
        idx += 1
        
restcnt = totalchange - cnt

if restcnt % 2 == 0:
    print(numbers)
else:
    numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
    print(numbers)
```

