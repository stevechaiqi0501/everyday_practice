N = int(input())
H = list(map(int,input().split()))

for i in range(1,len(H)):
    if H[0] < H[i]:
        print(H[i])
        break
    else:
        continue