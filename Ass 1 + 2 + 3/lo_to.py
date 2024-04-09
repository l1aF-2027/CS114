def check():
    loto = [input().split() for i in range(3)]

    so_phieu = int(input())

    so_loto = [int(input()) for i in range(so_phieu)]

    mark = [[0]*3 for i in range(3)]

    for m in so_loto:
        for i in range(3):
            for j in range(3):
                if loto[i][j] == str(m):
                    mark[i][j] = 1

    for i in range(3):
            if sum(mark[i]) == 3 or sum(mark[j][i] for j in range(3)) == 3:
                return ('Yes')

    if (mark[0][0] + mark[1][1] + mark[2][2]) == 3 or (mark[0][2] + mark[1][1] + mark[2][0]) == 3:
                return ('Yes')

    return ('No')

print(check())