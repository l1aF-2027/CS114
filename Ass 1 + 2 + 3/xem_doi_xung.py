import sys

def check_func(check, n):
        
    count = 0 
    for i in range(n//2):

        if (check[i] != check[n - 1 - i]):
            count = count + 1
            if count > 1:
                return "FALSE"
    return 'TRUE'

n = int(input())
check = [sys.stdin.readline() for i in range(n)]

print(check_func(check, n))