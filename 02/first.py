with open('input.txt', 'r') as file:
    reports = file.read().split('\n')

safe_count = 0
for report in reports:
    levels = [int(level) for level in report.split()]
    if len(levels) == 0:
        continue

    is_safe = True
    is_increasing = (levels[1] - levels[0]) > 0
    prev_level = levels[0]
    for level in levels[1:]:
        diff = level - prev_level
        if is_increasing and (diff < 1 or diff > 3):
            is_safe = False
            break
        if not is_increasing and (diff < -3 or diff > -1):
            is_safe = False
            break
        prev_level = level

    if is_safe:
        safe_count += 1
print(safe_count)