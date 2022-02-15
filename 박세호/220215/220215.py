# 백준 2805
n,m = map(int,input().split())
lst = list(map(int,input().split()))

min_ = 0
max_ = max(lst)
mid_ = (min_+max_)//2
## 이진탐색과 비슷한 구조의 반복문
while min_ <= max_:
    sum_ = 0
    mid_ = (min_ + max_) // 2
    for i in lst:
        if i - mid_ > 0:
            sum_ += (i-mid_)
    ## 매개변수 탐색으로 이진 탐색과 차이가 있음.
    if sum_ < m:
        max_ = mid_ - 1
    else:
        min_ = mid_ + 1

print(max_)
