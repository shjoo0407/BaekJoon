angles = [int(input()) for _ in range(3)]
angles.sort()

a,b,c = angles

if a + b + c != 180: # 세 각의 합이 180이 아닌 경우
    print('Error')
elif a == b == c: # 세 각이 모두 60인 경우
    print('Equilateral')
elif a == b or a == c or b == c:
    print('Isosceles')
else:
    print('Scalene')