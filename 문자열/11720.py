#숫자의 합
length = int(input())
str = input()
sum = 0
for i in range(length):
    sum = sum + int(str[i])

print(sum)