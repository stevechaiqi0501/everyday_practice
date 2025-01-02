# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

haystack = str(input())
needle = str(input())

Length_Haystack = len(haystack)
Needle_Haystack = len(needle)

flag = False

for i in range(Length_Haystack):
    if haystack[i:Needle_Haystack+i] is needle:
        print(i)
        flag = True
        
if not flag:
    print(-1)
        


