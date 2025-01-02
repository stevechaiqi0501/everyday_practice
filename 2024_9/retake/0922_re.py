# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

n = int(input())
counter = 0

def math_recursive(num:int) -> int:
    count = 1
    for i in range(1,num+1):
        count = count*i
        
    return count

temp = 0
count = 0
for i in range(0,(n//2)+1):
    temp = math_recursive(n-i)/(math_recursive((n-i)-i)*math_recursive(i))
    count += temp
        
        
    
print(int(count))
    
    
    


        

