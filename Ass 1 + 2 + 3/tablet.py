# Thư viện math để dùng hàm sqrt() để tính căn
import math

n = int(input())

count = 0

max = int(n / math.sqrt(2))
for a in range(1, max):
    # Định lý Pytago
    b_square = n * n - a * a
    # Lấy phần nguyên của căn b^2

    if math.sqrt(b_square).is_integer():
        count += 1

print(count)