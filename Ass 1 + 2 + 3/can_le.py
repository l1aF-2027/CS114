r, c = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(r)]
# max_len chatbox nó kêu thế này là nhanh nhất rồi ạ (https://chat.openai.com/share/54359c3f-7fcf-44ca-af4d-45e84035f013)
max_len = [max(map(lambda x: len(str(x)), col)) for col in zip(*grid)]

print_func = lambda row: print(" ".join(f"{val:>{max_len[j]}}" for j, val in enumerate(row)))
for row in grid:
    print_func(grid)