list_input = [5,2,4,6,1,3]
N = len(list_input)

for i in range(N):
    key = list_input[i]
    j = i -1
    while j >= 0 and key < list_input[j]:
        list_input[j+1] = list_input[j]
        j -= 1
    list_input[j+1] = key
    print(list_input)
    

print(list_input)
    