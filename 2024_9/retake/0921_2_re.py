import math

num = int(input())

num_root = math.sqrt(num)
num_root_con = num_root%1
result_num = num_root - num_root_con

print(int(result_num))