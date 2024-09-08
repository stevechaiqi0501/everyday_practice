# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
sum = list(map(int, input().split()))
target = list(map(int, input()))

def TwoSum(sum,target):
   
    prevMap = {}
    
    for i,n in enumerate(sum):
        diff = target - n
        if diff in prevMap:
            result_answer = [prevMap[diff],i]
            return result_answer
        prevMap[n] = i
    
print(TwoSum(sum,target))
        
        
    


