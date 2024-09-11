# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class SolutionsFor0911:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        ans = ""
        first_strs = strs[0]
        last_strs = strs[-1]
        for i in range(min(len(first_strs),len(last_strs))):
            if first_strs[i] != last_strs[i]:
                return ans
            ans += strs[i]
            
        return ans
    
Soltion = SolutionsFor0911()
print(Soltion(["flower","flow","flight"]))
