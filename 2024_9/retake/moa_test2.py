print("Enter first name:",end="")
first  = str(input())

print("Enter last name:",end="")
last = str(input())

print("Enter current salary:",end="")
sal = int(input())

def cal_new_sal(sal):
    
    if sal>=40000:
        new_sal = (sal + 2000) + (sal - 40000)*1.02
        
    if sal < 40000:
        new_sal = sal*1.05
        
    return new_sal

new_sal = cal_new_sal(sal)
print(f"New salary {first} {last} :",end="")
print(" ${:.2f}".format(new_sal))
    