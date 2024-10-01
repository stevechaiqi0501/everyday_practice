def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 最小値のインデックスを初期化
        min_index = i
        for j in range(i + 1, n):
            # 最小値を探す
            if arr[j] < arr[min_index]:
                min_index = j
        # 最小値を現在の位置に交換
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

        
        
