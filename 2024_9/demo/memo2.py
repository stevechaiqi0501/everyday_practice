# prctice for twosum

nums = list(map(int,input().split()))
target = int(input())
temp_numsDict = {}

for i in range(len(nums)):
    temp_numsDict[nums[i]] = i

for i in nums:
    digit = target - nums[i]
    if digit in temp_numsDict:
        print([temp_numsDict[digit],i])
    

    