# 그대로 출력하기
# 두 가지 방법이 있다.

#1.
import sys
while True:
    line = sys.stdin.readline().rstrip()
    if line!="":
        print(line)
    else:
        break
#
# #2.
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break
