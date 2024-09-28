input = list(map(int,input().split()))
count = 0
keep_input = []
for i in range(len(input)):
    if input[i] not in keep_input:
        keep_input.append(input[i])
    else:
        count += 1
        
keep_input.sort()
for i in range(count):
    keep_input.append("_")
    
print("output:",len(input)-count ,"result:",keep_input) 
        