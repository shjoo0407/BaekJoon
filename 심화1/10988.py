# 팰린드롬 확인하기
word = list(input())
word_rev = word[::-1]

if word==word_rev:
    print("1")
else:
    print("0")

