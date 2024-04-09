# Hàm rotate có tham khảo ở https://www.geeksforgeeks.org/complete-guide-on-2d-array-matrix-rotations/
def rotate_matrix(grid, r, c):
    if not len(grid):
        return
    if (c == 1):
        n = r
        if n <= 1:
            return grid
        temp = grid[n - 1][0]
        for i in range(n - 1, 0, -1):
            grid[i][0] = grid[i - 1][0]

        grid[0][0] = temp
        return grid
    if (r == 1):
        n = c
        if n <= 1:
            return grid
        temp = grid[0][n - 1]
        for i in range(n - 1, 0, -1):
            grid[0][i] = grid[0][i - 1]

        grid[0][0] = temp
        return grid
    
    top = 0
    bottom = len(grid) - 1
    left = 0
    right = len(grid[0]) - 1
    edge = -1

    while left < right and top < bottom:
        edge += 1
        if edge % 2 == 0: # Quay cùng chiều
            prev = grid[top + 1][left]

            for i in range(left, right + 1):
                grid[top][i], prev= prev, grid[top][i]
            top += 1
            for i in range(top, bottom + 1):
                grid[i][right], prev= prev, grid[i][right]
            right -= 1
            for i in range(right, left - 1, -1):
                grid[bottom][i], prev= prev, grid[bottom][i]
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                grid[i][left], prev= prev, grid[i][left]
            left += 1
        else: # Quay ngược chiều
            prev = grid[bottom - 1][left]
            for i in range(left, right + 1):
                grid[bottom][i], prev= prev, grid[bottom][i]
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                 grid[i][right], prev= prev, grid[i][right]
            right -= 1
            for i in range(right, left - 1, -1):
                grid[top][i], prev= prev, grid[top][i]
            top += 1
            for i in range(top, bottom + 1):
                grid[i][left], prev = prev, grid[i][left]
            left += 1
            
        if (right == left and bottom > top):
            if (edge + 1) % 2 == 0:
                temp = grid[bottom][right]
                for i in range(n, top, -1):
                    grid[i][right] = grid[i - 1][right]
                grid[top][right] = temp
            else: 
                temp = grid[top][right]
                for i in range(top, bottom):
                    grid[i][right] = grid[i + 1][right]
                grid[bottom][right] = temp
            return grid
        
        if (right > left and bottom == top):
            if (edge + 1) % 2 == 0:
                temp = grid[bottom][right]
                for i in range(right, left, -1):
                    grid[bottom][i] = grid[bottom][i - 1]
                grid[bottom][left] = temp
            else: 
                temp = grid[bottom][left]
                for i in range(left, right):
                    grid[bottom][i] = grid[bottom][i + 1]
                grid[bottom][right] = temp
            return grid
                

    return grid




r, c = map(int, input().split())
grid = [list(map(str, input().split())) for i in range(r)]
grid = rotate_matrix(grid, r, c)

for i in range(r):
    for j in range(c):
        print(grid[i][j], end = " ")
    print()
    
