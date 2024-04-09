# Hàm map (https://www.w3schools.com/python/ref_func_map.asp) đổi các input được split thành cũng một kiểu dữ liệu trong trường hợp này là int
item_prices = list(map(int, input().split()))
messages = []
for i in range(len(item_prices)):
    messages.append(input())
money = int(input())

import re

online_prices = 0
in_store_prices = 0

for i in range(len(item_prices)):
    price = item_prices[i]
    # Hàm re.search (https://laptrinhcanban.com/python/nhap-mon-lap-trinh-python/thao-tac-voi-chuoi-string-trong-python/tach-so-trong-chuoi-python/)
    percentage = 0
    if messages[i].find('%') != -1:
        match = re.search(r'(\d+)%', messages[i])
        if match:
            percentage = float(match.group(1))
    online_prices += price
    if 'lower' in messages[i]:
        in_store_prices += price * (1 + percentage/100)
    else:
        in_store_prices += price * (1 - percentage/100)
        
# Nếu tổng một trong hai cách mua bé hơn hoặc bằng tiền Bình có thì in ra true ngược lại thì false
if (min(online_prices, in_store_prices) <= money):
    print("true")
else:
    print("false")