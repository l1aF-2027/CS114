from collections import deque
import sys

lines = sys.stdin.readlines()
n, m = map(int, lines[0].split())
arr = [int(lines[i]) for i in range(1, n+ 1)]
operations = lines[n+1:n+m+1]

dq = deque(sorted(arr, reverse=True))

for op in operations:
    op = op.split()
    if op[0] == '-1':
        dq.popleft()
    elif op[0] == '-2':
        temp = dq[0]
        while dq and dq[0] == temp:
            dq.popleft()
    elif op[0] == '-3':
        temp = dq.popleft()
        dq.appendleft(int(temp) - int(op[1]))
    elif op[0] == '-4':
        temp = dq[0]
        while dq and dq[0] == temp:
            dq.popleft()
        dq.appendleft(int(temp) - int(op[1]))
    dq = deque(sorted(dq, reverse=True))

print(*dq, sep='\n')
