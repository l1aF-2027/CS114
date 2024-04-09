import bisect
import sys

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid + 1

def do(lines):
    arr = set()
    arr_= []
    temp_2  = []
    for i in lines[:-1]:
        temp = i.split()
        temp_1 = int(temp[1])
        if temp[0] == '1':
            if temp_1 not in arr:
                arr.add(temp_1)
                bisect.insort(arr_, temp_1)
        else:
                if temp_1 not in arr:
                    temp_2.append('0')
                else:
                    temp_2.append(str(binary_search(arr_,int(temp[1]))))
    return '\n'.join(temp_2)

lines = sys.stdin.readlines()
sys.stdout.write(do(lines))