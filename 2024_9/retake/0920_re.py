# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

digits = [1,2,4]
str_digits = ""
str_digit = list(map(str,digits))
for i in range(len(str_digit)):
    str_digits += str_digit[i]
    
ans = int(str_digits)
result = ans + 1
ans_list = []
for i in range(len(str(result))):
    temp_digit = result%10
    ans_list.append(temp_digit)
    result = result//10
    
ans_list.reverse()
    

print(ans_list)


# for i in range(len(str(result))):



