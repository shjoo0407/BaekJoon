a = int(input())
b = int(input())
quadrant = 0
if a>0:
    if b>0:
        quadrant = 1
    else:
        quadrant = 4
else:
    if b>0:
        quadrant = 2
    else:
        quadrant = 3

print(quadrant)

