with open(r"c:\Users\noahl\OneDrive - Grafisch Lyceum Rotterdam\Documents\projects\roblox\SCPRP\MergedGUI\Main.luau", "r", encoding="utf-8") as f:
    lines = f.readlines()

delete_ranges = [
    (959, 1078),
    (1199, 1707),
    (2217, 2553),
    (2891, 3176),
    (3463, 3639),
    (3817, 4208),
    (4601, 4929),
]

delete_set = set()
for start, end_ in delete_ranges:
    for i in range(start, end_ + 1):
        delete_set.add(i)

kept_lines = []
for i, line in enumerate(lines, 1):
    if i not in delete_set:
        kept_lines.append(line)

with open(r"c:\Users\noahl\OneDrive - Grafisch Lyceum Rotterdam\Documents\projects\roblox\SCPRP\MergedGUI\Main.luau", "w", encoding="utf-8") as f:
    f.writelines(kept_lines)

deleted = len(delete_set)
print(f"Deleted {deleted} lines from {len(lines)} -> {len(kept_lines)} lines")
print(f"Deleted ranges: {delete_ranges}")
