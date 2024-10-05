N = int(input())
*list_input, = list(map(int,input().split()))

flag = 1
count = 0
while flag:
    flag = 0
    for j in range(N-1,0,-1):
        if list_input[j] < list_input[j-1]:
            list_input[j],list_input[j-1] = list_input[j-1],list_input[j]
            count += 1
            print(list_input)
            flag = 1
        
        
print(*list_input)
print(count)
    