# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# a = str(input())
# b = str(input())

a = "1010"
b = "1011"

a_int = int(a)
b_int = int(b)

cal = 0

for i in range(len(a)):
    temp_a = a_int%10
    cal += temp_a * 2**i
    a_int = a_int//10
    
for i in range(len(b)):
    temp_b = b_int%10
    cal += temp_b * 2**i
    b_int = b_int//10

res = []
    
while True:
    if cal == 0:
        break
    if cal%2 == 0:
        res.append("0")
    else:
        res.append("1")
        
    cal = cal//2
    
ans_str = ""
    
for i in range(1,len(res)+1):
    ans_str = ans_str + res[-i]


if a == "0" and b == "0":
    print("0")
else:
    print(str(ans_str))
    


