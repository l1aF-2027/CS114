

def check_hang(i, j , r, c, grid, visited):
    for m in range(j + 1, c):
        if (grid[i][m] == '-'):
            visited[i][m] = True
        else: 
            break
    for m in range(j - 1, -1, -1):
        if (grid[i][m] == '-'):
            visited[i][m] = True
        else: 
            break

def check_cot(i, j , r, c, grid, visited):
    for m in range(i + 1, r):
        if (grid[m][j] == '-'):
            visited[m][j] = True
            if (c > m > 0):
                check_hang(m, j , r, c, grid, visited)
        else: 
            break
    for m in range(i - 1, -1, -1):
        if (grid[m][j] == '-'):
            visited[m][j] = True
            if (c > m > 0):
                check_hang(m, j , r, c, grid, visited)
        else: 
            break

def check(i, j , r, c, grid, visited):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    temp_i = i
    temp_j = j 
    for k in directions:
        temp_i = i + k[0]
        temp_j = j + k[1]
        while (0 <= temp_i < r and 0 <= temp_j < c and grid[temp_i][temp_j] == '-'):
            visited[temp_i][temp_j] = True 
            check_hang(temp_i, temp_j , r, c, grid, visited)
            check_cot(temp_i, temp_j , r, c, grid, visited)
            temp_i += k[0]
            temp_j += k[1]
        temp_i = i
        temp_j = j

def separate(lines):
    number_lines = []
    character_lines = []
    for line in lines:
        if any(char.isdigit() for char in line):
            number_lines.append(line)
        else:
            character_lines.append(line)
    return number_lines, character_lines

import fileinput
 
with fileinput.input(files=('a.txt', 'b.txt')) as f:

    number_lines, character_lines = separate(f)
    row, col = 0, 0
    result = []
    for i in number_lines:
        r, c = map(int, i.split())
        grid = [list(char for char in m) for m in character_lines[row:row + r]]
        row += r
        col += c
        count = 0 
        visited = [[False] * c for m in range(r)]

        for k in range(r):
            for l in range(c):

                if grid[k][l] == '-' and not visited[k][l]:
                    # print(str(k) + ' ,' + str(l))
                    count += 1
                    visited[k][l] = True
                    check(k, l, r, c, grid, visited)
        result.append(count)

    for i, val in enumerate(result):
        print('Case ' + str(i + 1) + ': ' + str(val))



