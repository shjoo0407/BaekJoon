# 그룹단어 체커
num = int(input())
cnt = num
for i in range(num):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        else:
            if word[j] in word[j+1:]:
                cnt = cnt-1
                break
print(cnt)



        

