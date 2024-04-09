r, c = map(int, input().split())

grid = []
for i in range(r):
    grid.append((input().split()))

for i in range(int(r/2)):
    grid[i], grid[-1-i] = grid[-1-i],grid[i]

for i in range(r):
    for j in grid[i]:
        print(j, end = " ")
    print()