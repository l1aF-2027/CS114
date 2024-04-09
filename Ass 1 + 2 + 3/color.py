from itertools import product

def count_ways(H, W, K, grid):
    count = 0

    # Hàm product trong thư viện intertools (https://www.geeksforgeeks.org/python-itertools-product/)
    # Taọ một tổ hợp chứa tất cả các lựa chọn True False có độ dài là H và W (tất cả cách chọn có thể tô đỏ của cả mạng lưới)
    for row in product([True, False], repeat = H):
        for col in product([True, False], repeat = W):
            black = 0
            for h in range(H):
                for w in range(W):
                    if (grid[h][w] == '#' and not (row[h] or col[w])):
                        black +=1
            if black == K:
                count += 1
    return count


H, W, K = map(int, input().split())
grid = [input() for i in range(H)]
print(count_ways(H, W, K, grid))  
