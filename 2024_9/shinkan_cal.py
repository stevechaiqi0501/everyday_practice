print("人数を入力してください")
numberOfMenber = int(input())
print("総額を入力してください")
cost = int(input())

cost_for_one = (cost + 1000)//numberOfMenber
if 1 < cost_for_one%100 and cost_for_one%100 < 50:
    payMoney = (cost_for_one//100)*100 + 50
    print("一人当たり、払わなければいけない値段は",payMoney,"です")
    
if 51 < cost_for_one%100 and cost_for_one%100 < 99:
    payMoney = (cost_for_one//100)*100 + 100
    print("一人当たり、払わなければいけない値段は",payMoney,"です")