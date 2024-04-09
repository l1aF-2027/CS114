n = int(input())
time = [list(map(float, input().split()))]
x, y, z= int(input()), int(input()), float(input())

temp = 0
count = 0
dmg = 0

for i in time[0]:
    dmg += x
    while (i - time[0][temp] > z):
        temp += 1
        count -= 1
    dmg += (count * y) 
    count += 1

print(int(dmg))