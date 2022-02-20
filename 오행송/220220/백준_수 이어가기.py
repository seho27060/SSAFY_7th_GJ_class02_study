
N = int(input())

n =0

maxlist=[]
while n < N:

    Nlist = [N, n]
    while 1:
        if Nlist[-2] >= Nlist[-1]:
            Nlist.append(Nlist[-2]-Nlist[-1])
        else:
            break
    if len(Nlist) > len(maxlist):
        maxlist = Nlist
    n += 1

print(len(maxlist))
print(*maxlist)