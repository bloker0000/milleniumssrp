import re

with open(r"c:\Users\noahl\OneDrive - Grafisch Lyceum Rotterdam\Documents\projects\roblox\SCPRP\MergedGUI\Main.luau", "r", encoding="utf-8") as f:
    lines = f.readlines()

depth = 0
keywords_close = re.compile(r'\b(end|until)\b')
elseif_re = re.compile(r'\belseif\b')
string_re = re.compile(r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')')

for i, raw_line in enumerate(lines, 1):
    line = raw_line.strip()
    if line.startswith("--"):
        continue
    cleaned = string_re.sub('""', line)
    cleaned = re.sub(r'--.*$', '', cleaned)
    
    if_count = len(re.findall(r'\bif\b', cleaned))
    elseifs = len(elseif_re.findall(cleaned))
    net_ifs = if_count - elseifs
    func_count = len(re.findall(r'\bfunction\b', cleaned))
    do_count = len(re.findall(r'\bdo\b', cleaned))
    repeat_count = len(re.findall(r'\brepeat\b', cleaned))
    closes = len(keywords_close.findall(cleaned))
    
    actual_opens = func_count + net_ifs + do_count + repeat_count
    change = actual_opens - closes
    
    if change != 0 and i >= 5100:
        old_depth = depth
        depth += change
        print(f"L{i:5d} [{old_depth:3d} -> {depth:3d}] {'+' if change > 0 else ''}{change}: {line[:100]}")
    else:
        depth += change

print(f"\nFinal depth: {depth}")
