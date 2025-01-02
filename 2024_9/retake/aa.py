A = 345
sum_digits = 0
while A != 0:
    sum_digits += A%10
    A = A//10

print(sum_digits)
    

# sum_digits = 0
# for number in range(1,1000001):
#     while number != 0:
#         sum_digits += number%10
#         number = number//10
        
# print(sum_digits)