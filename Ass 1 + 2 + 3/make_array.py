n = int(input())

arr = sorted(int(input()) for i in range(n))
check = set(arr)

count = 0 

for i in range(arr[0] + 1, arr[-1]):
    if i not in check:
        count += 1
print(count)