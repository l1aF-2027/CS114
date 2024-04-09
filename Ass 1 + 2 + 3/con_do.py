l, m = map(int, (input().split()))

queue = [[], []]

for i in range(m):
    length, side = input().split()
    if (side == 'left'):
        queue[0].append(int(length) / 100)
    else:
        queue[1].append(int(length) / 100)

side = 0
trip = 0

while queue[0] != [] or queue[1] != []:
    load = 0
    if (queue[side % 2]) == []:
        trip += 1
    else:
        while queue[side % 2] and ((load + queue[side % 2][0]) <= l):
            load += queue[side % 2].pop(0)
        trip += 1
    side += 1

print(trip)
