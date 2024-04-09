m, n = map(int, input().split())

grid = [input().split() for i in range(m)]

count = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == str(1):
            # print(str(i) + " " + str(j) + " " +str(count))
            if j != 0 and (grid[i][j - 1] == str(0)):
                count += 1
            if j != n - 1 and (grid[i][j + 1] == str(0)):
                count += 1
                # print('a')
            if i != 0 and (grid[i - 1][j] == str(0)):
                count += 1
            if i != m - 1 and (grid[i + 1][j] == str(0)):
                count += 1
            if i == 0:
                count += 1
            if j == 0:
                count += 1
            if i == m - 1:
                count += 1
            if j == n - 1:
                count += 1

print(count)
