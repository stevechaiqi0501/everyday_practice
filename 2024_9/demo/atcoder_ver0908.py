nums = [2,4,7,11]
target = 6

index_nums = {}

for i in range(len(nums)):
    index_nums[nums[i]] = i
    
for i in range(len(nums)):
    temp_nums = target - nums[i]
    if temp_nums in index_nums and index_nums[temp_nums] != i:
        print(index_nums[temp_nums],i)
    
