with open('input.txt', 'r') as file:
    data = file.read().split()

left = [int(data[i]) for i in range(0, len(data), 2)]
right = [int(data[i]) for i in range(1, len(data), 2)]

left.sort()
right.sort()

cum_diff = 0
for l, r in zip(left, right):
    cum_diff += abs(l - r)
print(cum_diff)