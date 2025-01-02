# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

nums = list(map(int,input().split()))
target = int(input())

if target in nums:
    print(nums.index(target))
else:
    nums.append(target)
    nums.sort()
    print(nums.index(target))

