### BJ 10828 스택

```python
import sys

N = int(sys.stdin.readline())

ST = []

for _ in range(N):

    order = sys.stdin.readline().rstrip()
    
    if order == 'top':
        if ST: print(ST[-1])
        else: print(-1)
    elif order == 'pop':
        if ST: p = ST.pop(); print(p)
        else: print(-1)
    elif order == 'size':
        print(len(ST))
    elif order == 'empty':
        if ST: print(0)
        else: print(1)
    else: # push
        order, num = order.split()
        ST.append(int(num))
```





### BJ 17479 재귀함수가 뭔가요?

```python
N = int(input())

def professor(N, cnt=0):

    txt1 = '____'* cnt + '''"재귀함수가 뭔가요?"\n'''
    txt2 = '____'* cnt + '''"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n'''
    txt3 = '____'* cnt + '''마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n'''
    txt4 = '____'* cnt + '''그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n'''
    suffix = '____'* cnt + '라고 답변하였지.\n'
    
    if N == 0:
        return txt1 + '____' * cnt + '"재귀함수는 자기 자신을 호출하는 함수라네"\n' + suffix
    return txt1 + txt2 + txt3 + txt4 + professor(N - 1, cnt + 1) + suffix

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
print(professor(N))


N = int(input())

def professor(num, cnt=0):
    if num == N:
        return '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n' + professor(num - 1, cnt + 1)

    txt1 = '____'* cnt + '''"재귀함수가 뭔가요?"\n'''
    txt2 = '____'* cnt + '''"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n'''
    txt3 = '____'* cnt + '''마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n'''
    txt4 = '____'* cnt + '''그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n'''
    suffix = '____'* cnt + '라고 답변하였지.\n'
    
    if num == 0:
        return txt1 + '____' * cnt + '"재귀함수는 자기 자신을 호출하는 함수라네"\n' + suffix
    return txt1 + txt2 + txt3 + txt4 + professor(num - 1, cnt + 1) + suffix

print(professor(N))

```

