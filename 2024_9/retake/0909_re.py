# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

class Solution:
    def reverse(self,input:int) -> int:
        
        if input < 0:
            return 0
        
        else:
            count = 0
            temp = input
            
            while temp<0:
               temp_num = temp%10
               count = count*10 + temp_num
               temp = temp//10
               
            if count == input:
                return "True"
            
        