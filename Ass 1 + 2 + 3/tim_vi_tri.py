# Em có tham khảo trên github cách giảm sử dụng bộ nhớ bằng class nên em đã thay hàm bằng class (https://www.phamduytung.com/blog/2019-02-06-how-to-reduce-memory-consumption-by-half-by-adding-just-one-line-of-code/)
import sys
class Dict:
    def __init__(self, s):
        self.arr = s.split()
        self.num_dict = {}
        for i, num in enumerate(self.arr):
            self.num_dict[num] = i
        del self.arr
    def find_index(self, key):
        return self.num_dict.get(key, -1)


n = int(input())
del n
arr = Dict(input())
m = int(input())
del m
find = input().split()
# print ("sys.getsizeof(dy):", sys.getsizeof(arr))

for i in find:
    print(arr.find_index(i))