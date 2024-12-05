with open('input.txt', 'r') as file:
    data = file.read().split()

left = [int(data[i]) for i in range(0, len(data), 2)]
right = [int(data[i]) for i in range(1, len(data), 2)]

left_dict = {}
for x in left:
    if x in left_dict:
        left_dict[x] += 1
    else:
        left_dict[x] = 1

right_dict = {}
for x in right:
    if x in right_dict:
        right_dict[x] += 1
    else:
        right_dict[x] = 1

score = 0
for key, value in left_dict.items():
    if key in right_dict:
        score += key * value * right_dict[key]
print(score)