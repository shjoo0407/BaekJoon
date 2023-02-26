# 크로아티아 알파벳
word = input()
alpha_lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for alpha in alpha_lst:
    if alpha in word:
        word = word.replace(alpha,"0")

print(len(word))