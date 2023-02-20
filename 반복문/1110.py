# 더하기 사이클
first_num = input()

while True:
    tmp = first_num
    if int(tmp)<10:
        tmp = "0" + tmp
    else:
        sum = str(int(tmp[0])+int(tmp[1]))
        new = first_num[-1]+sum[-1]

    if 


