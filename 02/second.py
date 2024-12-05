def is_safe(levels):
    is_increasing = (levels[1] - levels[0]) > 0
    prev_level = levels[0]
    for level in levels[1:]:
        diff = level - prev_level
        if is_increasing and (diff < 1 or diff > 3):
            return False
        if not is_increasing and (diff < -3 or diff > -1):
            return False
        prev_level = level
    return True

with open('input.txt', 'r') as file:
    reports = file.read().split('\n')

safe_count = 0
for report in reports:
    levels = [int(level) for level in report.split()]
    if len(levels) == 0:
        continue

    is_report_safe = is_safe(levels)
    if not is_report_safe:
        for discarded in range(len(levels)):
            is_report_safe = is_safe(levels[:discarded] + levels[(discarded + 1):])
            if is_report_safe:
                break

    if is_report_safe:
        safe_count += 1

print(safe_count)