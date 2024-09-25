# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

strs = ["flower","flow","flight"]
first_strs = strs[0]
last_strs = strs[-1]

for i in range((min(len(first_strs),len(last_strs)))):
    if first_strs[i] != last_strs[i]:
        print(first_strs[0:i])
        break
        