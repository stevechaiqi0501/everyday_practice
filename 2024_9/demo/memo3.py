# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# x = int(input)
x = 321

if x<0:
    print("False")
else:
    x_str = str(x)
    int_num = 0
    for i in range(len(x_str)):
        digit = x % 10
        int_num = int_num*10 + digit 
        x = x//10
        
if int_num == x:
    print(True)
else:
    print(False)
