# 단어공부
word = input().upper()
unique_word = list(set(word))

cnt_list = []
for a in unique_word:
    cnt = word.count(a)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list))>1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_word[max_index])



