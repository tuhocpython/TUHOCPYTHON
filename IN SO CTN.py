L = int (input())
R = int (input())
ctn=0
while L <= R:
    if L % 2 == 0:
        ctn += 1
    L += 1
print(L)
print(ctn)