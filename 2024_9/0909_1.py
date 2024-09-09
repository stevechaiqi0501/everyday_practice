# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
x = int(input())

if x < 0:
    print("False")
else:
    reversed_num = 0
    temp = x
    
    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10  # temp を10で割って、次の桁に進む

    # reversed_num が x と一致するかどうかを確認
    if reversed_num == x:
        print("True")
    else:
        print("False")