a = int(input())
answer = 0
if ((a % 4 == 0) & (a % 100 != 0))|(a%400==0):
    answer = 1
else:
    pass

print(answer)
