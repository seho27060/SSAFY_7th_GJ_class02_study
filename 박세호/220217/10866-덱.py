import sys
nums = int(sys.stdin.readline())
### sys 안써서 시간초과 나는 문제 ^^!!
lst = []

for i in range(nums):
    order_ = sys.stdin.readline().split() ## split을 하게 되면 list로 입력된다.
    if len(order_) >= 2:                  ## order_에 접근할려면 order_[0]으로 해야함.
        if order_[0][:4] == "push":
            if order_[0][4:] == "_front":
                lst.insert(0,int(order_[1]))
            elif order_[0][4:] == "_back":
                lst.append(int(order_[1]))
    elif order_[0][:3] == "pop":
        if len(lst) == 0:
            print(-1)
        elif order_[0][3:] == "_front":
            print(lst.pop(0))
        else:
            print(lst.pop(-1))
    elif order_[0] == "size":
        print(len(lst))
    elif order_[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif order_[0] == "front":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    else:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])

