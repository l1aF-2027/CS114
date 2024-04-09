n = int(input())

grid = [list(map(int, input().replace('‐', '-').split())) for i in range(n)]

count = 0

for i in range(2, n):
    x1, y1 = grid[i - 2][0], grid[i - 2][1]
    x2, y2 = grid[i - 1][0], grid[i - 1][1]
    x3, y3 = grid[i][0], grid[i][1]

    vec1 = [(x2 - x1), (y2 - y1)]
    vec2 = [(x3 - x2), (y3 - y2)]
    
    if not (vec2[0] - vec1[0] == 0 or vec2[1] - vec1[1] == 0 ):
        if (vec1[0] > 0 and vec2[1] < 0):
            count += 1
        if (vec1[0] < 0 and vec2[1] > 0):
            count += 1
        if (vec1[1] > 0 and vec2[0] > 0):
            count += 1
        if (vec1[1] < 0 and vec2[0] < 0):
            count += 1
        
print(count)