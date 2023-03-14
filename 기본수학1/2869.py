# 달팽이는 올라가고 싶다.
import sys

a,b,v = map(int,input().split())

day = 1
sum = 0

while True:
    sum = sum + a
    if sum >= v:
        break
    else:
        sum = sum - b
    day = day + 1

print(day)
