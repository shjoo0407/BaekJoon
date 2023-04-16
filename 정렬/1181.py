# 단어 정렬하기

n = int(input())
lst = []
for i in range(n):
    word = input()
    if word not in lst:
        lst.append(word)


lst.sort()
lst.sort(key=len)
# 길이가 짧은거 부터
# 선택정렬

# for i in range(len(lst)):
#     min_idx = i
#     for j in range(i+1, len(lst)):
#         if len(lst[j]) < len(lst):
#             min_idx = j
#         elif len(lst[j]) == len(lst[min_idx]):
#             if lst[j] < lst[min_idx]:
#                 min_idx = j
#     lst[i],lst[min_idx] = lst[min_idx],lst[i]

for i in lst:
    print(i)

# 람다함수를 쓰면 간단해진다
# import sys
#
# n = int(sys.stdin.readline())
# words = []
#
# for _ in range(n):
#     word = sys.stdin.readline().rstrip()
#     if word not in words: # 중복 제거
#         words.append(word)
#
# words.sort() # 사전순 정렬
# words.sort(key=lambda x: len(x)) # 길이순 정렬
#
# for word in words:
#     print(word)
