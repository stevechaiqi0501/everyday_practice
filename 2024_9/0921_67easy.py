# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

input_a = "1011" 
input_b = "1010"

a_10int = int(input_a,2)
b_10int = int(input_b,2)

result_10int = a_10int + b_10int
result_2int = bin(result_10int)

output = str(result_2int)[2:]
print(output)