input_int = int(input())

before_int = input_int
output = 0

if input_int < 0:
    print("false")
else:
    while input_int != 0:
        ones_place = input_int % 10
        output = output*10 + ones_place
        input_int //= 10
        
        if before_int == output:
            print("ok")