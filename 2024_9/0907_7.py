
while True:
    H,W=map(int,input().split())
    if H == 0 and W == 0:
        break
    
    
    for i in range(W):
        for j in range(H):
            if (i+j)%2 == 0:
                print("#",end="")
            else:
                print(".",end="")
        print()

