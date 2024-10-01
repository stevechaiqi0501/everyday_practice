import math
input_int = int(input())

root_inputInt = math.sqrt(input_int)

dec = root_inputInt % 1

if dec>1:
    print(root_inputInt)
else:
    print(root_inputInt-dec)