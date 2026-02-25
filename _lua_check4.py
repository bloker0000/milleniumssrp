import re

with open(r"c:\Users\noahl\OneDrive - Grafisch Lyceum Rotterdam\Documents\projects\roblox\SCPRP\MergedGUI\Main.luau", "r", encoding="utf-8") as f:
    lines = f.readlines()

depth = 0
string_re = re.compile(r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')')

for i, raw_line in enumerate(lines, 1):
    line = raw_line.strip()
    if line.startswith("--"):
        continue
    cleaned = string_re.sub('""', line)
    cleaned = re.sub(r'--.*$', '', cleaned)
    
    opens = 0
    opens += len(re.findall(r'\bfunction\b', cleaned))
    opens += len(re.findall(r'\bif\b', cleaned))
    opens += len(re.findall(r'\bdo\b', cleaned))
    opens += len(re.findall(r'\brepeat\b', cleaned))
    
    closes = 0
    closes += len(re.findall(r'\bend\b', cleaned))
    closes += len(re.findall(r'\buntil\b', cleaned))
    
    change = opens - closes
    old = depth
    depth += change
    
    if change != 0 and 4880 <= i <= 4940:
        print(f"L{i:5d} [{old:3d} -> {depth:3d}] {'+' if change > 0 else ''}{change}: {line[:120]}")

print(f"\nDepth at L4940: {depth}")
