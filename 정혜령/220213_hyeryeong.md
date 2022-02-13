### 백준 소인수 분해

```python
N = int(input())

def isPrime(number):
    if number > 1: 
        for num in range(2, number):
            if number % num == 0:
                return False
        else:
            return True

def func(number):
    if isPrime(number):
        print(number)
        return number
    for n in range(2, number):
        if isPrime(n) and number % n== 0:
            number //= n
            print(n)
            return func(number)

func(N)
```

대충 재귀로 풀었는데....? 되긴 하는데...?

천천히 올라가니 너무 살 떨린다.



다른 사람 코드 보니 훨씬 간단하던데 역시 제곱근으로 하는 법을 공부해야하나보다.

```python
n = int(input())

# 소인수분해 + 제곱근
for i in range(2, int(n ** 0.5) + 1) :
    if n % i == 0 :
        while n % i == 0 :
            print(i)
            n //= i

if(n > 1) :
    print(n)
```

