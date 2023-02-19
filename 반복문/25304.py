#영수증
total = int(input())
item_num = int(input())
sum = 0
for i in range(item_num):
    price, amount = map(int,input().split())
    sum = sum + (price * amount)

if sum == total:
    print("Yes")
else:
    print("No")