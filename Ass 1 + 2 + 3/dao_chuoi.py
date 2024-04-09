# Em có đọc tham khảo một số cách làm tại trang https://oj.vnoi.info/problem/icpc23_regional_f nhưng code là em tự viết và đã đọc hiểu

t = int(input())
test_cases = []
for _ in range(t):
    a = input()
    b = input()
    test_cases.append((a, b))

for i in range(t):
    # Hàm sorted (https://www.w3schools.com/python/ref_func_sorted.asp) để sắp xếp lại chuỗi theo thứ tự tăng dần, so sánh nếu khác nhau thì in ra NO
    if sorted(test_cases[i][0]) != sorted(test_cases[i][1]):
        print("NO")
    else:
        # Vì đây là đảo chuỗi có độ dài lẻ nên chắc chắn các phần tử ở vị trí lẻ sẽ vẫn sẽ ở vị trí lẻ, chẵn thì vẫn ở chắn
        # Lấy các phần tử ở vị trí chẵn ra 
        odd_a = test_cases[i][0][0::2]
        odd_b = test_cases[i][1][0::2]
        # Lấy các phần tử vị trí lẻ ra
        even_a = test_cases[i][0][1::2]
        even_b = test_cases[i][1][1::2]
        
        if (sorted(odd_a) == sorted(odd_b) and sorted(even_a) == sorted(even_b)):
            print("YES")
        else:
            print("NO")