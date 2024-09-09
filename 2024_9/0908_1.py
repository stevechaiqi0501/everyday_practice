# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

nums = list(map(int,input().split()))#[2,7,11,13]
target = int(input())# 9

hashMap = {}
for i in range(len(nums)):
   hashMap[nums[i]] = i
   #この時点で[0:2 , 1:7 , 2:11 , 3:13]という辞書が出来上がる
   
print(hashMap)

for i in range(len(nums)):
    
    conplement = target - nums[i]
    if conplement in hashMap and hashMap[conplement] != i:
        print([hashMap[conplement],i])
    
        
        
        