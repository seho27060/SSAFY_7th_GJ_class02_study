###쉬운 거스름돈 SWEA-1970
nums = int(input())

for tc in range(nums):
    target = input()
    if target[-1] != "0":
        target = target[:-1]+"0"
    target = int(target)
    moneys = [50000,10000,5000,1000,500,100,50,10]
    pocket =[0]*len(moneys)
    check = False
    for i in range(len(moneys)):
        get_ = target
        for j in range(len(moneys[:i+1])):
            if moneys[j] <= get_:
                pocket[j] = get_//moneys[j]
                get_ -= pocket[j]*moneys[j]
            if get_ == 0:
                check = True
                break
        if check:
            pocket = list(map(str,pocket))
            print("#{0}\n{1}".format(tc+1, " ".join(pocket)))
            break
