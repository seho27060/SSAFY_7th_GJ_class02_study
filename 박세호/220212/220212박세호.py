nums = int(input())


for tc in range(nums):
    n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    sort_lst = sorted(lst,reverse=True)
    lst2 = []

    for i in range(len(lst)):
        lst2.append([i, lst[i]])

    loc = 0
    count = 0
    while 1:
        if lst2[0][1] == sort_lst[0]:
            count += 1
            if lst2[0][0] == m:
                print(count)
                break
            else:
                lst2.pop(0)
                sort_lst.pop(0)

        else:
            get_ = lst2.pop(0)
            lst2.append(get_)

