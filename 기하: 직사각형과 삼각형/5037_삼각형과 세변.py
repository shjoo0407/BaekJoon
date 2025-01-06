while True:
    a,b,c = map(int, input().split())
    a,b,c = sorted([a,b,c])
    if a==0 and b==0 and c==0:
        break
    else:
        if c>=a+b:
            print("Invalid")
        elif a==b==c:
            print("Equilateral")
        elif a==b or b==c or a==c:
            print("Isosceles")
        elif a!=b and b!=c and a!=c:
            print("Scalene")