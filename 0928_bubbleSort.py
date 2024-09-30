# A = [5,3,2,4,1]
# for i in range(len(A)+1):
#     key = A[-i]
#     j = -i-1
#     while key < A[j] and j >= -i-1:
#         A[j+1] = A[j]
#         j -= 1
#     A[j+1] = key
        
        
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 最後のi個は既にソートされているので、その分だけ減らす
        for j in range(0, n - i - 1):
            # 隣接要素を比較して、順序が逆であれば交換
            if arr[j] > arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 使用例
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)
    