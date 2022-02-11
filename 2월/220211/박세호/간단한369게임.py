### 간단한 369 게임
nums = int(input())

for i in range(1,nums+1):
    count = 0
    check = False
    for j in str(i):
        if j in ["3","6","9"]:
            count += 1
            check = True
    if check:
        print("-"*count, end=" ")
    else:
        print(str(i),end=" ")
