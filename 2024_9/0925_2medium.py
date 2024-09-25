# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.



l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

l1.reverse()
l2.reverse()

l1_int = int(''.join(map(str,l1)))
l2_int = int(''.join(map(str,l2)))

result_int = l1_int + l2_int
result_str = str(result_int)
result = []

for i in range(len(result_str)):
    result.append(int(result_str[i]))

result.reverse()
print(result)