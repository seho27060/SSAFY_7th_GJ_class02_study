### BJ

```python
import sys

T = int(input())

Queue = [0] * 2_000_001
front = rear = -1

for _ in range(T):
    order = sys.stdin.readline().rstrip()

    if order == 'pop':
        if front != rear:
            front += 1
            print(Queue[front])
        else: print(-1)
    elif order == 'size':
        print(rear - front)
        # front -1 rear 0 -> 하나 있다
        # rear - front = 1
    elif order == 'empty':
        if front == rear: print(1)
        else: print(0)
    elif order == 'front':
        if front != rear:
            print(Queue[front + 1])
        else: print(-1)
    elif order == 'back':
        if front != rear:
            print(Queue[rear])
        else: print(-1)
    else:
        order, num = order.split()
        num = int(num)
        rear += 1
        Queue[rear] = num
```





### BJ 2164 카드2

```python
N = int(input())
cards = [0] * (N * 2)
front, rear = 0, N

for num in range(1, N + 1):
    cards[num] = num

while rear - front != 1:
    # dequeue
    front += 1
    if rear - front == 1:
        print(cards[rear])
        break
    # dequeue + enqueue
    front += 1
    card = cards[front]
    rear += 1
    cards[rear] = card
else: print(cards[rear])
```

