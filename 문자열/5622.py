#다이얼
words = input()
alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
num = 0
for i in range(len(words)):
    for j in alpha:
        if words[i] in j:
            num = num + alpha.index(j) + 3

print(num)