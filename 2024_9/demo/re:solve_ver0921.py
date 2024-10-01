input_a = "1011" 
input_b = "1010"

a_10int = int(input_a,2)
b_10int = int(input_b,2)

result_10int = a_10int + b_10int
result = bin(result_10int)
print(result[2:])