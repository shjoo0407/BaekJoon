# ACM 호텔

t = int(input())
for i in range(t):
    h,w,n = map(int,input().split())
    floor = str(n%h)
    room_num = n//h+1
    if room_num < 10:
        room_num = '0'+ str(room_num)
    else:
        room_num = str(room_num)
    print(floor+room_num)








