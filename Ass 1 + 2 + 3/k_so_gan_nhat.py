import sys
def cost(i):
    return abs(i - x)

def printres(arr, k):
    arr.sort(key=cost)
    print(*sorted(arr[:k]))

lines = sys.stdin.readlines()
n = int(lines[0])
arr = list(map(int, lines[1].split()))
k, x = map(int,lines[2].split())

printres(arr, k)