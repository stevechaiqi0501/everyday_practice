# prctice for twosum
# # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

nums = [2,7,11,15]
target = 9

#index_nums ={2:0,7:1,11:2,15:3}

index_nums = {}
for i in range(len(nums)):
    index_nums[nums[i]] = i
    
for i in range(len(nums)):
    digit = target - nums[i]
    if digit in nums and index_nums[digit] != i:
        print(i,index_nums[digit])
