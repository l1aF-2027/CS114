m, n = map(int, input().split())

onlines = input().split()
friends = set(input().split())
count = 0
for i in onlines:
    if (i in friends):
        count += 1
    if (count == n):
        break
print(count)
