# ACM 호텔

t = int(input())
for i in range(t):
    h,w,n = map(int,input().split())
    floor = n%h
    room_num = n//h+1
    if n%h == 0:
        room_num = n//h
        floor = h

    print(f'{floor*100+room_num}')










