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
    
    old = depth
    depth += opens - closes
    
    if depth < 0 and old >= 0:
        print(f"WENT NEGATIVE at L{i}: depth {old} -> {depth}: {line[:100]}")
    if depth == 0 and old != 0 and i > 100:
        print(f"RETURNED TO 0 at L{i}: {line[:80]}")

print(f"\nFinal depth: {depth}")
if depth == 0:
    print("BALANCED")
elif depth > 0:
    print(f"{depth} unclosed block(s)")
else:
    print(f"{abs(depth)} extra end(s)")
