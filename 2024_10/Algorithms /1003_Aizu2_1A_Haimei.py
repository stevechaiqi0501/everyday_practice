A = [5,3,4,2,1]
N = len(A)
flag = 1
while flag:
    flag = 0
    for j in range(N-1,0,-1):
        print(A)
        if A[j] < A[j-1]:
            A[j],A[j-1] = A[j-1],A[j]
            flag = 1
        
        
        
        
        
#  bubbleSort(A, N) // N 個の要素を含む 0-オリジンの配列 A
# 2   flag = 1 // 逆の隣接要素が存在する
# 3   while flag
# 4     flag = 0
# 5     for j が N-1 から 1 まで
# 6       if A[j] < A[j-1]
# 7         A[j] と A[j-1] を交換
# 8         flag = 1
        
    
        
# for i in range(N-1,-1,-1):
#     if list_input[i] < list_input[i-1]:
#         list_input[i],list_input[i-1] = list_input[i-1],list_input[i]
# print(list_input)
        