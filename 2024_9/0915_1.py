# class Solutions:
#     def RemoveDuplicates():
        
nums = list(map(int,input().split()))
nums.sort()
resultNums_int = []
resultNums_str = []
resultNums_int.append(nums[0])
count = 1

for i in range(1,len(nums)):
    if nums[i] == nums[i-1]:
        nums[i] = "_"
        resultNums_str.append(nums[i])
        
    else:
        resultNums_int.append(nums[i])
        count += 1
        
resultNums = []
for i in resultNums_int:
    resultNums.append(i)
    
for i in resultNums_str:
    resultNums.append(i)
    
k = count

print("result :",resultNums,"k= ",k)
        
                
        
            
            