N = int(input()) #3,6,1,2,4,5
*A, = list(map(int,input().split()))

for i in range(N):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        i -= 1
    A[j+1] = key

        
