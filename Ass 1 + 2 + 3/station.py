# Tạo ma trận 2x2
station = [['', ''], ['', '']]

# Nhập giá trị vào ma trận
for i in range(2):
    a = input()
    station[i][0], station[i][1] = a[0], a[1]
if sum(row.count('#') for row in station) == 2:
    if station[0][0] == '#' and station[1][1] == '#':
        print("No")
    elif station[0][1] == '#' and station[1][0] == '#':
        print("No")
    else:
        print("Yes")
else:
    print("Yes")