print("Enter your age:",end="")
age = int(input())

print("Enter number of months of servise:",end="")
month = int(input())

print("Enter first of three higest salaries:",end="")
first = float(input())

print("Enter second of three highest salaries:",end="")
second = float(input())

print("Enter third of three highest salaries:",end="")
third = float(input())

def cal_ave(first_dem,second_dem,third_dem):
    
    ave = (first_dem + second_dem + third_dem)/3
    return ave

def cal_p(month_dem):
    yrs= month_dem/12
    per = 0
    
    if yrs >= 0 and yrs <=5:
        per = yrs*1.5
        
    if yrs >5 and yrs <= 10:
        per = 7.5 + (yrs-5)*1.75
        
    if yrs >10:
        per = 7.5 + 8.75 + (yrs-10)*2.0


    perRate = per


    if perRate >= 80:
        p = 80
    else:
        p = perRate
        
    return p*0.01

result = cal_p(month)*cal_ave(first,second,third)
print("Annual persion: ${:.2f}".format(result))
    

