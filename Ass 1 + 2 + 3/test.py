import bisect
import sys

def binary_search(arr, key, low, high):
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid
    return low

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i)
        arr[j+1:i+1] = arr[j:i]
        arr[j] = key
            
def do(lines):
    arr = set()
    arr_= []
    temp_1 = []
    for i in lines[:-1]:
        temp = i.split()
        if temp[0] == '1':
            if temp[1] not in arr:
                arr.add(int(temp[1]))
                bisect.insort(arr_,int(temp[1]))
        # else:
        #     if int(temp[1]) not in arr:
        #         temp_1.append('0')
        #     else:
        #         idx = binary_search(arr_,int(temp[1]))
    #     #         temp_1.append(str(idx))
    # return '\n'.join(temp_1)
                

lines = sys.stdin.readlines()
(do(lines))
