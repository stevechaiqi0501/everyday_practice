input_nums = [1,2,3,4]

input_int = int(''.join(map(str,input_nums)))
result_int = input_int + 1
result_str = str(result_int)
result = []
for i in range(len(result_str)):
    result.append(result_str[i])
    
print(result)