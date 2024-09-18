# nums = list(map(int,input().split()))
# value = int(input())

nums = [1,2,3,2,3,2]
value = 2
count = 0

for i in range(0,len(nums)):
    if nums[i] == value:
        nums[i] = "_"
        count += 1
        
print(nums)

temp_nums = []
temp_nums_ = []
for i in nums:
    if i == "_":
        temp_nums_.append(i)
    else:
        temp_nums.append(i)
        
print(temp_nums,temp_nums_)

        
temp_nums.sort()
temp_nums.extend(temp_nums_) #その関数がなにを返すのか理解する
print(temp_nums)
        

        
        
        