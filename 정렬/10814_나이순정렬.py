import sys

N = int(sys.stdin.readline())
user_lst = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    user_lst.append((int(age),name))

user_lst.sort(key=lambda x:x[0])
for i in user_lst:
    print(i[0],i[1])