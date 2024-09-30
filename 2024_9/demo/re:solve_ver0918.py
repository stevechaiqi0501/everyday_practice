list_num = list(map(int,input().split()))
target = int(input())

if target in list_num:
    print(list_num.index(target))
else:
    for i in range(len(list_num)):
        if list_num[i] > target:
            list_num.insert(i,target)
            break
print(list_num)