#  selectionSort(A, N) // N個の要素を含む0-オリジンの配列A
# 2   for i が 0 から N-1 まで
# 3     minj = i
# 4     for j が i から N-1 まで
# 5       if A[j] < A[minj]
# 6         minj = j
# 7     A[i] と A[minj] を交換

N = int(input())
A = list(map(int,input().split()))

for i in range(0,N):
    minj = i
    for j in range(i,N):
        if A[j] < A[minj]:
            minj = j
            A[i],A[minj] = A[minj],A[j]
            print(A)
