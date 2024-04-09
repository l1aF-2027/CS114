import math

ax, ay = map(int, input().split(' '))
bx, by = map(int, input().split(' '))


d = math.sqrt((ax-bx)**2 + (ay-by)**2)
# TH 1
dx, dy = (bx - ax) , (by - ay)

# Tính tọa độ của hai điểm còn lại của hai hình vuông

c1 = (int(bx + dy), int(by - dx))
d1 = (int(ax + dy), int(ay - dx))


square_vertices_1 = []
square_vertices_1.append((ax, ay))
square_vertices_1.append((bx, by))
square_vertices_1.append(c1)
square_vertices_1.append(d1)

c2 = (int(ax - dy), int(ay + dx))
d2 = (int(bx - dy) , int(by + dx))

square_vertices_2 = []
square_vertices_2.append((ax, ay))
square_vertices_2.append(c2)
square_vertices_2.append(d2)
square_vertices_2.append((bx, by))

for i,square in enumerate(square_vertices_2):
    if i != 3:
        print(square, end = " ")
    else: 
        print(square)
for i,square in enumerate(square_vertices_1):
    if i != 3:
        print(square, end = " ")
    else: 
        print(square)