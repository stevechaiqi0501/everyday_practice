# head = list(map(int,input().split()))
head = [1,1,1,1,1,1,2,2,3,4,5,6,7,8,8,8,9,]

passed_list = []
passed_list.append(head[0])

for i in range(1,len(head)):
    if head[i] != head[i-1]:
        passed_list.append(head[i])
        
        
print(passed_list)
    